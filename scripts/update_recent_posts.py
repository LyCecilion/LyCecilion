#!/usr/bin/env python3
"""Update the CrystaRin post list in README.md from its Atom feed."""

from __future__ import annotations

import argparse
import calendar
from datetime import datetime, timezone
from pathlib import Path
import sys
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET


FEED_URL = "https://crystal.stellalyr.ink/atom.xml"
START_MARKER = "<!-- CRYSTARIN-POSTS:START -->"
END_MARKER = "<!-- CRYSTARIN-POSTS:END -->"
ATOM = "{http://www.w3.org/2005/Atom}"


def four_months_before(moment: datetime) -> datetime:
    month_index = moment.year * 12 + moment.month - 1 - 4
    year, zero_based_month = divmod(month_index, 12)
    month = zero_based_month + 1
    day = min(moment.day, calendar.monthrange(year, month)[1])
    return moment.replace(year=year, month=month, day=day)


def fetch_feed(source: str) -> bytes:
    if source.startswith(("http://", "https://")):
        request = Request(source, headers={"User-Agent": "LyCecilion-profile-updater/1.0"})
        with urlopen(request, timeout=30) as response:
            return response.read()
    return Path(source).read_bytes()


def recent_posts(feed: bytes, cutoff: datetime) -> list[tuple[datetime, str, str]]:
    root = ET.fromstring(feed)
    posts: list[tuple[datetime, str, str]] = []

    for entry in root.findall(f"{ATOM}entry"):
        title = entry.findtext(f"{ATOM}title")
        published_text = entry.findtext(f"{ATOM}published")
        link_element = entry.find(f"{ATOM}link[@rel='alternate']") or entry.find(
            f"{ATOM}link"
        )
        link = link_element.get("href") if link_element is not None else None
        if not title or not published_text or not link:
            continue

        published = datetime.fromisoformat(published_text.replace("Z", "+00:00"))
        if published >= cutoff:
            posts.append((published, title.strip(), link))

    return sorted(posts, key=lambda post: post[0], reverse=True)


def update_readme(path: Path, posts: list[tuple[datetime, str, str]]) -> bool:
    original = path.read_text(encoding="utf-8")
    if original.count(START_MARKER) != 1 or original.count(END_MARKER) != 1:
        raise ValueError("README must contain exactly one CrystaRin marker pair")

    before, remainder = original.split(START_MARKER, 1)
    _, after = remainder.split(END_MARKER, 1)
    lines = [f"- [{title}]({link})" for _, title, link in posts]
    replacement = f"{START_MARKER}\n" + "\n".join(lines) + f"\n{END_MARKER}"
    updated = before + replacement + after

    if updated == original:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--feed", default=FEED_URL)
    parser.add_argument("--readme", type=Path, default=Path("README.md"))
    parser.add_argument(
        "--now",
        type=lambda value: datetime.fromisoformat(value.replace("Z", "+00:00")),
        default=datetime.now(timezone.utc),
        help="Override the current time (ISO 8601), primarily for testing",
    )
    args = parser.parse_args()

    now = args.now
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    cutoff = four_months_before(now.astimezone(timezone.utc))
    posts = recent_posts(fetch_feed(args.feed), cutoff)
    if not posts:
        print("No posts found in the last four months; refusing to clear README", file=sys.stderr)
        return 1

    changed = update_readme(args.readme, posts)
    print(f"Found {len(posts)} posts; README {'updated' if changed else 'unchanged'}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
