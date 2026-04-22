#!/usr/bin/env python3
"""Detect likely React/TypeScript and FastAPI scaffold locations in a repository.

This script is intentionally heuristic. It helps a future Codex run inspect a repo
before generating a feature scaffold; it should not replace reading nearby code.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Iterable


IGNORE_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".idea",
    ".vscode",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "node_modules",
    "dist",
    "build",
    ".next",
    ".venv",
    "venv",
    "env",
}

THIS_FILE = Path(__file__).resolve()

FRONTEND_DIR_NAMES = {
    "src",
    "app",
    "client",
    "frontend",
    "web",
    "pages",
    "routes",
    "features",
    "components",
    "hooks",
    "api",
    "services",
    "types",
}

BACKEND_DIR_NAMES = {
    "app",
    "server",
    "backend",
    "api",
    "routers",
    "routes",
    "endpoints",
    "services",
    "schemas",
    "models",
    "crud",
    "repositories",
}


def iter_files(root: Path, max_depth: int) -> Iterable[Path]:
    root = root.resolve()
    for current, dirs, files in os.walk(root):
        current_path = Path(current)
        depth = len(current_path.relative_to(root).parts)
        dirs[:] = [name for name in dirs if name not in IGNORE_DIRS and depth < max_depth]
        for filename in files:
            path = current_path / filename
            if path.resolve() == THIS_FILE:
                continue
            yield path


def iter_dirs(root: Path, max_depth: int) -> Iterable[Path]:
    root = root.resolve()
    for current, dirs, _ in os.walk(root):
        current_path = Path(current)
        depth = len(current_path.relative_to(root).parts)
        dirs[:] = [name for name in dirs if name not in IGNORE_DIRS and depth < max_depth]
        for dirname in dirs:
            yield current_path / dirname


def read_text(path: Path, limit: int = 120_000) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")[:limit]
    except OSError:
        return ""


def score_path(path: Path, names: set[str]) -> int:
    parts = {part.lower() for part in path.parts}
    return sum(1 for name in names if name in parts)


def find_package_json(root: Path) -> list[Path]:
    return [path for path in iter_files(root, 4) if path.name == "package.json"]


def find_python_manifests(root: Path) -> list[Path]:
    names = {"pyproject.toml", "requirements.txt", "Pipfile", "poetry.lock"}
    return [path for path in iter_files(root, 4) if path.name in names]


def detect_frontend(root: Path, max_depth: int) -> dict[str, object]:
    package_files = find_package_json(root)
    react_packages: list[str] = []
    ts_packages: list[str] = []

    for package_file in package_files:
        text = read_text(package_file)
        if '"react"' in text or "'react'" in text:
            react_packages.append(str(package_file))
        if "typescript" in text or '"tsx"' in text:
            ts_packages.append(str(package_file))

    candidates: list[tuple[int, str]] = []
    for path in iter_dirs(root, max_depth):
        if path.name.lower() in FRONTEND_DIR_NAMES:
            candidates.append((score_path(path, FRONTEND_DIR_NAMES), str(path)))

    candidates.sort(key=lambda item: (-item[0], item[1]))

    return {
        "package_json": [str(path) for path in package_files],
        "react_package_json": react_packages,
        "typescript_signals": ts_packages,
        "likely_directories": [path for _, path in candidates[:20]],
    }


def detect_backend(root: Path, max_depth: int) -> dict[str, object]:
    manifests = find_python_manifests(root)
    fastapi_files: list[str] = []
    router_files: list[str] = []

    for path in iter_files(root, max_depth):
        if path.suffix != ".py":
            continue
        text = read_text(path, 40_000)
        if "FastAPI(" in text or "from fastapi" in text or "import fastapi" in text:
            fastapi_files.append(str(path))
        if "APIRouter" in text or ".include_router(" in text:
            router_files.append(str(path))

    candidates: list[tuple[int, str]] = []
    for path in iter_dirs(root, max_depth):
        if path.name.lower() in BACKEND_DIR_NAMES:
            candidates.append((score_path(path, BACKEND_DIR_NAMES), str(path)))

    candidates.sort(key=lambda item: (-item[0], item[1]))

    return {
        "python_manifests": [str(path) for path in manifests],
        "fastapi_signals": fastapi_files[:40],
        "router_signals": router_files[:40],
        "likely_directories": [path for _, path in candidates[:20]],
    }


def find_similar_modules(root: Path, feature: str | None) -> list[str]:
    if not feature:
        return []

    tokens = [token.lower() for token in feature.replace("_", "-").split("-") if token]
    if not tokens:
        tokens = [feature.lower()]

    matches: list[str] = []
    for path in iter_dirs(root, 6):
        name = path.name.lower()
        if any(token in name for token in tokens):
            matches.append(str(path))
        if len(matches) >= 40:
            return matches

    for path in iter_files(root, 6):
        name = path.name.lower()
        if any(token in name for token in tokens):
            matches.append(str(path))
        if len(matches) >= 40:
            return matches
    return matches


def build_suggested_tree(feature: str | None) -> dict[str, list[str]]:
    slug = (feature or "feature").strip().replace(" ", "-").replace("_", "-").lower()
    slug = "-".join(part for part in slug.split("-") if part) or "feature"
    pascal = "".join(part.capitalize() for part in slug.split("-"))
    snake = slug.replace("-", "_")

    return {
        "frontend_fallback": [
            f"src/features/{slug}/{pascal}Page.tsx",
            f"src/features/{slug}/components/{pascal}Panel.tsx",
            f"src/features/{slug}/api.ts",
            f"src/features/{slug}/hooks.ts",
            f"src/features/{slug}/types.ts",
            f"src/features/{slug}/index.ts",
        ],
        "backend_fallback": [
            f"app/{snake}/router.py",
            f"app/{snake}/service.py",
            f"app/{snake}/schemas.py",
            f"app/{snake}/crud.py",
        ],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Detect likely scaffold patterns for React TS + FastAPI projects.")
    parser.add_argument("--root", default=".", help="Repository root to inspect.")
    parser.add_argument("--feature", default=None, help="Optional feature name to search for similar modules.")
    parser.add_argument("--format", choices={"json", "text"}, default="text", help="Output format.")
    parser.add_argument("--max-depth", type=int, default=6, help="Maximum file walk depth for focused scans.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()

    if not root.exists():
        raise SystemExit(f"Root does not exist: {root}")

    result = {
        "root": str(root),
        "frontend": detect_frontend(root, args.max_depth),
        "backend": detect_backend(root, args.max_depth),
        "similar_modules": find_similar_modules(root, args.feature),
        "suggested_fallback_tree": build_suggested_tree(args.feature),
        "note": "Use these findings as hints only; read nearby files before editing.",
    }

    if args.format == "json":
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"Root: {result['root']}")
        print("\nFrontend signals:")
        for item in result["frontend"]["likely_directories"][:10]:
            print(f"  - {item}")
        print("\nBackend signals:")
        for item in result["backend"]["likely_directories"][:10]:
            print(f"  - {item}")
        print("\nSimilar modules:")
        for item in result["similar_modules"][:10]:
            print(f"  - {item}")
        print("\nSuggested fallback tree:")
        for group, paths in result["suggested_fallback_tree"].items():
            print(f"  {group}:")
            for path in paths:
                print(f"    - {path}")
        print(f"\nNote: {result['note']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
