#!/usr/bin/env python3
"""Collect compact development context for daily dev diary drafting.

The script is intentionally conservative: it gathers evidence but does not
generate the diary. Use the output as raw material for the skill workflow.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from dataclasses import dataclass, asdict
from datetime import date, datetime, time, timedelta
from pathlib import Path
from typing import Iterable


TODO_RE = re.compile(r"\b(TODO|FIXME|BUG|HACK|NOTE)\b[:：]?\s*(.*)", re.IGNORECASE)
SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    "node_modules",
    "dist",
    "build",
    ".next",
    ".venv",
    "venv",
    "__pycache__",
    ".idea",
    ".vscode",
}
TEXT_EXTS = {
    ".c",
    ".cc",
    ".cpp",
    ".cs",
    ".css",
    ".go",
    ".h",
    ".html",
    ".java",
    ".js",
    ".jsx",
    ".json",
    ".kt",
    ".md",
    ".php",
    ".py",
    ".rb",
    ".rs",
    ".scss",
    ".sh",
    ".sql",
    ".swift",
    ".toml",
    ".ts",
    ".tsx",
    ".txt",
    ".yaml",
    ".yml",
}


@dataclass
class Context:
    repo: str
    git_root: str | None
    scope: str | None
    since: str
    until: str | None
    commits: list[str]
    committed_files: list[str]
    status: list[str]
    unstaged_files: list[str]
    staged_files: list[str]
    diff_stat: list[str]
    todos: list[str]
    warnings: list[str]


def run(command: list[str], cwd: Path) -> tuple[int, str, str]:
    proc = subprocess.run(
        command,
        cwd=str(cwd),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        errors="replace",
    )
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def git(cwd: Path, args: list[str]) -> tuple[bool, list[str]]:
    code, stdout, _ = run(["git", *args], cwd)
    if code != 0:
        return False, []
    return True, [line for line in stdout.splitlines() if line.strip()]


def resolve_since(raw: str) -> str:
    value = raw.strip().lower()
    now = datetime.now()
    if value in {"today", "today 00:00"}:
        return datetime.combine(date.today(), time.min).isoformat(timespec="minutes")
    if value in {"yesterday"}:
        return datetime.combine(date.today() - timedelta(days=1), time.min).isoformat(
            timespec="minutes"
        )
    if value in {"week", "this-week", "this week"}:
        start = date.today() - timedelta(days=date.today().weekday())
        return datetime.combine(start, time.min).isoformat(timespec="minutes")
    if value in {"7d", "last-7-days"}:
        return (now - timedelta(days=7)).isoformat(timespec="minutes")
    return raw


def collect_todos(root: Path, limit: int) -> list[str]:
    matches: list[str] = []
    for path in root.rglob("*"):
        if len(matches) >= limit:
            break
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if not path.is_file() or path.suffix.lower() not in TEXT_EXTS:
            continue
        try:
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        for lineno, line in enumerate(lines, start=1):
            found = TODO_RE.search(line)
            if not found:
                continue
            rel = path.relative_to(root)
            text = found.group(0).strip()
            matches.append(f"{rel}:{lineno}: {text}")
            if len(matches) >= limit:
                break
    return matches


def collect_context(args: argparse.Namespace) -> Context:
    repo = Path(args.repo).resolve()
    since = resolve_since(args.since)
    until = args.until
    warnings: list[str] = []

    ok, root_lines = git(repo, ["rev-parse", "--show-toplevel"])
    git_root = root_lines[0] if ok and root_lines else None
    git_cwd = Path(git_root) if git_root else repo
    scope: str | None = None
    scope_args: list[str] = []
    if git_root:
        try:
            relative_scope = repo.relative_to(Path(git_root).resolve())
            if relative_scope != Path("."):
                scope = relative_scope.as_posix()
                scope_args = ["--", scope]
        except ValueError:
            warnings.append(
                f"{repo} is inside git root {git_root}, but scope resolution failed."
            )

    commits: list[str] = []
    committed_files: list[str] = []
    status: list[str] = []
    unstaged_files: list[str] = []
    staged_files: list[str] = []
    diff_stat: list[str] = []

    if git_root:
        log_args = [
            "log",
            f"--since={since}",
            "--date=short",
            "--pretty=format:%h\t%ad\t%s",
        ]
        if until:
            log_args.insert(2, f"--until={until}")
        _, commits = git(git_cwd, log_args + scope_args)

        file_args = [
            "log",
            f"--since={since}",
            "--name-status",
            "--date=short",
            "--pretty=format:commit %h %ad %s",
        ]
        if until:
            file_args.insert(2, f"--until={until}")
        _, committed_files = git(git_cwd, file_args + scope_args)

        _, status = git(git_cwd, ["status", "--short", *scope_args])
        _, unstaged_files = git(git_cwd, ["diff", "--name-status", *scope_args])
        _, staged_files = git(git_cwd, ["diff", "--cached", "--name-status", *scope_args])
        if args.include_diff_stat:
            _, diff_stat = git(git_cwd, ["diff", "--stat", "HEAD", *scope_args])
    else:
        warnings.append(f"{repo} is not a git repository; git sections are empty.")

    todos = [] if args.no_todos else collect_todos(repo, args.max_todos)

    return Context(
        repo=str(repo),
        git_root=git_root,
        scope=scope,
        since=since,
        until=until,
        commits=commits,
        committed_files=committed_files,
        status=status,
        unstaged_files=unstaged_files,
        staged_files=staged_files,
        diff_stat=diff_stat,
        todos=todos,
        warnings=warnings,
    )


def section(title: str, lines: Iterable[str]) -> str:
    body = list(lines)
    if not body:
        body = ["(none)"]
    return "\n".join([f"## {title}", "", *body, ""])


def render_markdown(context: Context) -> str:
    parts = [
        "# Development Context Snapshot",
        "",
        f"- Repo: `{context.repo}`",
        f"- Git root: `{context.git_root or 'none'}`",
        f"- Scope: `{context.scope or 'repository root'}`",
        f"- Since: `{context.since}`",
        f"- Until: `{context.until or 'now'}`",
        "",
    ]
    if context.warnings:
        parts.append(section("Warnings", [f"- {item}" for item in context.warnings]))
    parts.append(section("Commits", [f"- {item}" for item in context.commits]))
    parts.append(section("Committed Files", [f"- {item}" for item in context.committed_files]))
    parts.append(section("Working Tree Status", [f"- {item}" for item in context.status]))
    parts.append(section("Unstaged Files", [f"- {item}" for item in context.unstaged_files]))
    parts.append(section("Staged Files", [f"- {item}" for item in context.staged_files]))
    parts.append(section("Diff Stat", [f"- {item}" for item in context.diff_stat]))
    parts.append(section("TODO Markers", [f"- {item}" for item in context.todos]))
    return "\n".join(parts).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Collect git, diff, status, and TODO context for dev diary drafting."
    )
    parser.add_argument("--repo", default=".", help="Repository or project path.")
    parser.add_argument(
        "--since",
        default="today",
        help='Start time passed to git log, or one of: today, yesterday, this-week, 7d.',
    )
    parser.add_argument("--until", default=None, help="Optional end time passed to git log.")
    parser.add_argument(
        "--include-diff-stat",
        action="store_true",
        help="Include git diff --stat HEAD for uncommitted changes.",
    )
    parser.add_argument(
        "--no-todos",
        action="store_true",
        help="Skip scanning source files for TODO/FIXME/BUG/HACK/NOTE markers.",
    )
    parser.add_argument("--max-todos", type=int, default=40, help="Maximum TODO markers.")
    parser.add_argument(
        "--format",
        choices=["markdown", "json"],
        default="markdown",
        help="Output format.",
    )
    args = parser.parse_args()

    context = collect_context(args)
    if args.format == "json":
        print(json.dumps(asdict(context), ensure_ascii=False, indent=2))
    else:
        print(render_markdown(context), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
