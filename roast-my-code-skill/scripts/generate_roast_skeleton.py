#!/usr/bin/env python3
"""Generate a reusable roast-style code review skeleton."""

import argparse


ZH_HEADINGS = {
    "impression": "## 总体印象",
    "points": "## 最值得吐槽的 3~5 点",
    "serious": "## 真正严重的问题",
    "good": "## 其实还不错的地方",
    "summary": "## 一句话总结",
}

EN_HEADINGS = {
    "impression": "## Overall Impression",
    "points": "## Top 3-5 Roast-Worthy Findings",
    "serious": "## Actually Serious Issues",
    "good": "## What Is Actually Good",
    "summary": "## One-Line Summary",
}


def clamp_points(value: int) -> int:
    return max(3, min(5, value))


def zh_template(mode: str, intensity: str, points: int) -> str:
    tone = "正式审查" if mode == "formal" else f"{mode}/{intensity}"
    sections = [
        f"<!-- mode: {mode}; intensity: {intensity}; tone: {tone} -->",
        ZH_HEADINGS["impression"],
        "",
        "<一句有趣但克制的话；formal 模式下改为直接工程判断。>",
        "",
        ZH_HEADINGS["points"],
        "",
    ]
    for index in range(1, points + 1):
        sections.extend(
            [
                f"### {index}. <吐槽标题> `[severity: high|medium|low|nit|preference]` `[type: true issue|style preference]`",
                "",
                "- 问题说明：<引用文件/函数/行号，说明具体问题。>",
                "- 为什么值得吐槽：<轻巧吐槽；formal 模式下改成直接原因。>",
                "- 可能影响：<bug、维护成本、性能、API、安全或测试影响。>",
                "- 建议改法：<具体下一步；必要时给短代码片段。>",
                "",
            ]
        )
    sections.extend(
        [
            ZH_HEADINGS["serious"],
            "",
            "- <只列 high severity。没有就写：基于当前上下文，没看到 high severity 问题。>",
            "",
            ZH_HEADINGS["good"],
            "",
            "- <真实优点 1。>",
            "- <真实优点 2，可选。>",
            "- <真实优点 3，可选。>",
            "",
            ZH_HEADINGS["summary"],
            "",
            "<幽默收尾，但要包含可执行方向。>",
        ]
    )
    return "\n".join(sections)


def en_template(mode: str, intensity: str, points: int) -> str:
    tone = "formal review" if mode == "formal" else f"{mode}/{intensity}"
    sections = [
        f"<!-- mode: {mode}; intensity: {intensity}; tone: {tone} -->",
        EN_HEADINGS["impression"],
        "",
        "<One concise, lightly funny impression; use direct engineering judgment in formal mode.>",
        "",
        EN_HEADINGS["points"],
        "",
    ]
    for index in range(1, points + 1):
        sections.extend(
            [
                f"### {index}. <Roast title> `[severity: high|medium|low|nit|preference]` `[type: true issue|style preference]`",
                "",
                "- Problem: <Cite file/function/line and state the concrete issue.>",
                "- Why it deserves the roast: <Short roast; use direct cause in formal mode.>",
                "- Impact: <Bug, maintenance, performance, API, security, or testing impact.>",
                "- Suggested fix: <Concrete next step; include a short code snippet if useful.>",
                "",
            ]
        )
    sections.extend(
        [
            EN_HEADINGS["serious"],
            "",
            "- <List only high-severity issues. If none: No high-severity issue is visible from the available context.>",
            "",
            EN_HEADINGS["good"],
            "",
            "- <Real strength 1.>",
            "- <Real strength 2, optional.>",
            "- <Real strength 3, optional.>",
            "",
            EN_HEADINGS["summary"],
            "",
            "<Humorous close, but include an actionable direction.>",
        ]
    )
    return "\n".join(sections)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a roast-style code review skeleton."
    )
    parser.add_argument("--mode", choices=["roast", "balanced", "formal"], default="roast")
    parser.add_argument(
        "--intensity", choices=["mild", "medium", "spicy"], default="medium"
    )
    parser.add_argument("--points", type=int, default=4, help="Number of roast points, 3-5.")
    parser.add_argument("--language", choices=["zh", "en"], default="zh")
    args = parser.parse_args()

    points = clamp_points(args.points)
    intensity = "mild" if args.mode == "formal" else args.intensity
    if args.language == "zh":
        print(zh_template(args.mode, intensity, points))
    else:
        print(en_template(args.mode, intensity, points))


if __name__ == "__main__":
    main()
