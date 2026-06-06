from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
readme = ROOT / "README.md"
now = datetime.now(timezone(timedelta(hours=8)))
content = readme.read_text(encoding="utf-8")

def replace(content, start, end, body):
    before, rest = content.split(start, 1)
    _, after = rest.split(end, 1)
    return f"{before}{start}\n{body}{end}{after}"

header = (ROOT / "templates" / ("header-odd.md" if now.day % 2 else "header-even.md")).read_text(encoding="utf-8")
techstack = (ROOT / "templates" / ("techstack-odd.md" if now.isocalendar().week % 2 else "techstack-even.md")).read_text(encoding="utf-8")

content = replace(content, "<!-- HEADER_START -->", "<!-- HEADER_END -->", header)
content = replace(content, "<!-- TECHSTACK_START -->", "<!-- TECHSTACK_END -->", techstack)
readme.write_text(content, encoding="utf-8")
