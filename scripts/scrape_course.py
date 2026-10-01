#!/usr/bin/env python3
"""Scrape the public UAIC Software Security course page.

Default behaviour:
  * save a local HTML snapshot;
  * extract all links with their visible labels;
  * classify same-origin PDF links and external references;
  * write scrape-output/links.json.

Use --download-same-origin to also download same-origin linked files into
materials/. Both output directories are git-ignored on purpose.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import urllib.parse
import urllib.request
from html.parser import HTMLParser

COURSE_URL = "https://edu.info.uaic.ro/securitate-software/"
USER_AGENT = "UAIC-course-archive/1.0 (+personal academic archive)"


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[dict[str, str]] = []
        self._href: str | None = None
        self._text: list[str] = []

    def handle_starttag(self, tag: str, attrs):
        if tag.lower() != "a":
            return
        attrs = dict(attrs)
        self._href = attrs.get("href")
        self._text = []

    def handle_data(self, data: str):
        if self._href is not None:
            self._text.append(data)

    def handle_endtag(self, tag: str):
        if tag.lower() != "a" or self._href is None:
            return
        label = re.sub(r"\s+", " ", "".join(self._text)).strip()
        self.links.append({"href": self._href, "label": label})
        self._href = None
        self._text = []


def request_bytes(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as response:
        return response.read()


def safe_filename(url: str) -> str:
    path = urllib.parse.urlparse(url).path
    name = pathlib.PurePosixPath(path).name or "index.html"
    return urllib.parse.unquote(name)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default=COURSE_URL)
    parser.add_argument("--output", default="scrape-output")
    parser.add_argument("--download-same-origin", action="store_true")
    args = parser.parse_args()

    output = pathlib.Path(args.output)
    output.mkdir(parents=True, exist_ok=True)

    html_bytes = request_bytes(args.url)
    html = html_bytes.decode("utf-8", errors="replace")
    (output / "course-page.html").write_text(html, encoding="utf-8")

    p = LinkParser()
    p.feed(html)

    base = urllib.parse.urlparse(args.url)
    records = []
    for item in p.links:
        absolute = urllib.parse.urljoin(args.url, item["href"])
        parsed = urllib.parse.urlparse(absolute)
        same_origin = (parsed.scheme, parsed.netloc) == (base.scheme, base.netloc)
        records.append({
            "label": item["label"],
            "url": absolute,
            "same_origin": same_origin,
            "is_pdf": parsed.path.lower().endswith(".pdf"),
        })

    seen = set()
    deduped = []
    for record in records:
        if record["url"] in seen:
            continue
        seen.add(record["url"])
        deduped.append(record)

    (output / "links.json").write_text(
        json.dumps(deduped, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    if args.download_same_origin:
        target = pathlib.Path("materials")
        target.mkdir(parents=True, exist_ok=True)
        for record in deduped:
            if not record["same_origin"]:
                continue
            parsed = urllib.parse.urlparse(record["url"])
            if parsed.scheme not in {"http", "https"}:
                continue
            destination = target / safe_filename(record["url"])
            try:
                destination.write_bytes(request_bytes(record["url"]))
                print(f"downloaded {record['url']} -> {destination}")
            except Exception as exc:
                print(f"failed {record['url']}: {exc}")

    print(f"found {len(deduped)} unique links")
    print(f"wrote {output / 'course-page.html'}")
    print(f"wrote {output / 'links.json'}")


if __name__ == "__main__":
    main()
