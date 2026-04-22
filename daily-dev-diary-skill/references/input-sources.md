# Input Sources And Priority

Use this reference when collecting evidence for a daily dev diary, daily/weekly report, or concise development summary.

## Source Priority

1. User-provided goals, notes, meeting records, and manual work logs.
2. Git commits in the requested time range.
3. Git diff, changed files, diff stats, and uncommitted changes.
4. Issues, TODOs, checklists, tickets, and project task records.
5. Error logs, failed tests, debugging notes, and fix records.
6. Historical conversation context and nearby project context.

Prefer direct user statements over inferred intent from code. Prefer newer and more explicit sources over older or vague sources.

## Practical Collection

When the user provides enough notes, use those as the main source and use git/logs only to verify or enrich.

When the user asks to generate from git, collect:

- Commit subjects and dates for the requested period.
- Changed file names and diff stats.
- Uncommitted staged/unstaged changes if the diary should include current work.
- TODO/FIXME markers only when relevant to the requested scope.

Useful git commands:

```bash
git log --since="today 00:00" --date=short --pretty=format:"%h %ad %s"
git log --since="1 week ago" --name-status --date=short --pretty=format:"commit %h %ad %s"
git diff --name-status
git diff --stat
git status --short
```

The bundled helper can collect a compact snapshot:

```bash
python scripts/collect_dev_context.py --repo /path/to/repo --since today
python scripts/collect_dev_context.py --repo /path/to/repo --since "2026-04-01" --until "2026-04-07"
```

## Conflict Handling

- If user notes say the task is incomplete but commits look finished, write "阶段性完成/已提交部分实现，仍有待确认项".
- If commits say "fix" but logs show failures remain, write "进行了修复调整，但验证仍未通过/仍需继续排查".
- If file changes suggest one feature but the user names another goal, organize around the user's named goal and mention file-level evidence only as support.
- If the time range is ambiguous, use the user's latest phrasing. If still ambiguous, default to "today" for daily diary requests and state the assumption briefly.

## Evidence Interpretation

Treat these as higher-confidence signals:

- User says the goal or result directly.
- Commit message includes specific task or issue ID.
- Tests or logs show before/after state.
- Diff includes named modules, route names, UI copy, or test names that match the stated task.

Treat these as lower-confidence signals:

- Only filenames are available.
- Commit messages are vague, such as "update", "fix", "wip", or "cleanup".
- Large generated files dominate the diff.
- The work appears only as uncommitted changes.

With low-confidence evidence, use conservative wording and avoid definitive business claims.
