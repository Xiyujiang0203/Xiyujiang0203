from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
readme = ROOT / "README.md"
now = datetime.now(timezone(timedelta(hours=8)))
odd = now.toordinal() % 2 == 1
content = readme.read_text(encoding="utf-8")

def replace(content, start, end, body):
    before, rest = content.split(start, 1)
    _, after = rest.split(end, 1)
    return f"{before}{start}\n{body}{end}{after}"

def load(name):
    return (ROOT / "templates" / f"{name}-{'odd' if odd else 'even'}.md").read_text(encoding="utf-8")

for section in ("header", "activity-mid", "techstack", "activity-bottom"):
    content = replace(content, f"<!-- {section.upper().replace('-', '_')}_START -->", f"<!-- {section.upper().replace('-', '_')}_END -->", load(section))

readme.write_text(content, encoding="utf-8")
