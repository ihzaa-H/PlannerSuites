#!/usr/bin/env python3
"""Stamp a fresh build id into version.json and every app page.

Run this before committing a change you want live:

    python scripts/stamp_build.py

Why commit-time and not build-time: this repo is published by TWO deployers on
every push -- the "Deploy to GitHub Pages" Actions workflow and GitHub's own
"pages-build-deployment" branch builder. The branch builder publishes the raw
repository content, so anything stamped only inside the workflow gets
overwritten. Stamping here means both deployers publish identical, correctly
stamped files.

Each page compares its stamp against version.json on load and reloads once if
they differ, which defeats GitHub Pages' fixed 10-minute cache.
"""
import datetime as _dt
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = [
    ROOT / "construction-planner" / "home.html",
    ROOT / "construction-planner" / "flowchart.html",
    ROOT / "construction-planner" / "whiteboard.html",
    ROOT / "construction-planner" / "index.html",
]
PATTERN = re.compile(r'(window\.__BUILD_ID__=")[^"]*(")')


def main() -> int:
    build = _dt.datetime.now(_dt.timezone.utc).strftime("%Y%m%d-%H%M%S")

    (ROOT / "version.json").write_text(
        json.dumps({"build": build}) + "\n", encoding="utf-8"
    )

    missing, stamped = [], []
    for page in PAGES:
        if not page.exists():
            missing.append(page.name)
            continue
        text = page.read_text(encoding="utf-8")
        new_text, count = PATTERN.subn(rf"\g<1>{build}\g<2>", text)
        if not count:
            missing.append(page.name + " (no build id marker)")
            continue
        page.write_text(new_text, encoding="utf-8", newline="")
        stamped.append(page.name)

    print(f"build {build}")
    print("stamped: " + ", ".join(stamped))
    if missing:
        print("WARNING, not stamped: " + ", ".join(missing), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
