"""Build the launch-plan outputs from content.py.

Usage: python3 tools/build_workbook.py
Outputs:
  deliverables/AI_Dad_Launch_Plan.xlsx   one tab per section
  deliverables/AI_Dad_Launch_Plan.csv    single tab, sections stacked (the Google Sheet layout)
  deliverables/sheet_paste.html          the same single-tab layout as an HTML table, for the in-place Sheets update
  docs/LAUNCH_PLAN.md                    readable copy
"""
import csv
import html
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill

sys.path.insert(0, os.path.dirname(__file__))
import content  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
XLSX = os.path.join(ROOT, "deliverables", "AI_Dad_Launch_Plan.xlsx")
CSV = os.path.join(ROOT, "deliverables", "AI_Dad_Launch_Plan.csv")
HTML = os.path.join(ROOT, "deliverables", "sheet_paste.html")
MD = os.path.join(ROOT, "docs", "LAUNCH_PLAN.md")

HEADER_FILL = PatternFill("solid", fgColor="1F2937")
HEADER_FONT = Font(bold=True, color="FFFFFF")
WRAP = Alignment(wrap_text=True, vertical="top")


def utf16_len(s):
    """Character count the way the apps' counters see it (an emoji counts as 2)."""
    return len(s.encode("utf-16-le")) // 2


def bio_copy(platform, field):
    for row in content.BIO[3]:
        if row[0] == platform and row[1] == field:
            return row[2]
    raise KeyError((platform, field))


def stacked_rows(tabs):
    """The single-tab Google Sheet layout: every section stacked, in order."""
    rows = [["AI DAD HEALTHY DAD: LAUNCH PLAN (sections below, in order)"],
            ["Sections: " + " · ".join(t[0] for t in tabs)]]
    for title, intro, header, body in tabs:
        rows.append([])
        rows.append([f"■ {title.upper()}"])
        rows.extend([line] for line in intro)
        rows.append(list(header))
        rows.extend(list(r) for r in body)
    return rows


def fill_placeholders(tabs):
    """Replace {ROWS} and the bio character counts with real values."""
    values = {
        "{TT_BIO_LEN}": str(utf16_len(bio_copy("TikTok", "Bio"))),
        "{IG_NAME_LEN}": str(utf16_len(bio_copy("Instagram", "Name"))),
        "{IG_BIO_LEN}": str(utf16_len(bio_copy("Instagram", "Bio"))),
        # Filling text never adds rows, so the count is stable.
        "{ROWS}": str(len(stacked_rows(tabs))),
    }

    def fill(cell):
        cell = str(cell)
        for key, val in values.items():
            cell = cell.replace(key, val)
        return cell

    return [(fill(t), [fill(i) for i in intro], [fill(h) for h in header], [[fill(c) for c in r] for r in body])
            for t, intro, header, body in tabs], values


def col_width(header, rows, i):
    longest = max([len(str(header[i]))] + [min(len(str(r[i])), 400) for r in rows])
    return max(10, min(70, int(longest / 3.2) + 8)) if longest > 30 else max(10, longest + 4)


def build_xlsx(tabs):
    wb = Workbook()
    wb.remove(wb.active)
    for title, intro, header, rows in tabs:
        ws = wb.create_sheet(title[:31])
        r = 1
        for line in intro:
            ws.cell(row=r, column=1, value=line).font = Font(italic=True)
            r += 1
        r += 1 if intro else 0
        header_row = r
        for c, h in enumerate(header, 1):
            cell = ws.cell(row=r, column=c, value=h)
            cell.fill, cell.font, cell.alignment = HEADER_FILL, HEADER_FONT, WRAP
        for row in rows:
            r += 1
            for c, v in enumerate(row, 1):
                # Stored as string cells so Sheets keeps "1", "#" etc. as text on import.
                cell = ws.cell(row=r, column=c, value=str(v))
                cell.alignment = WRAP
                cell.data_type = "s"
        for i in range(len(header)):
            ws.column_dimensions[chr(65 + i)].width = col_width(header, rows, i)
        ws.freeze_panes = ws.cell(row=header_row + 1, column=1)
    os.makedirs(os.path.dirname(XLSX), exist_ok=True)
    wb.save(XLSX)


def build_csv(rows):
    with open(CSV, "w", newline="") as f:
        csv.writer(f).writerows(rows)


def build_html(rows):
    """One-line HTML table. No double quotes, backslashes or raw newlines survive,
    so the string can sit inside a JSON body untouched. Rows aren't padded: the
    update clears the sheet first, so short rows can't leave stale cells behind."""

    def td(v):
        # Only &, <, > and " need escaping; apostrophes are safe in both HTML text and JSON.
        v = html.escape(str(v), quote=False).replace('"', "&quot;").replace("\n", "<br>")
        return f"<td>{v}</td>"

    out = ["<table>"]
    for r in rows:
        cells = list(r) or [""]
        out.append("<tr>" + "".join(td(c) for c in cells) + "</tr>")
    out.append("</table>")
    page = "".join(out)
    assert '"' not in page and "\\" not in page and "\n" not in page
    with open(HTML, "w") as f:
        f.write(page)
    return page


def md_cell(v):
    return str(v).replace("\n", "<br>")


def build_md(tabs):
    out = ["# AI Dad Healthy Dad: Launch Plan", "",
           "Generated from `tools/content.py`. The same content lives in the project Google Sheet.", ""]
    for title, intro, header, rows in tabs:
        out += [f"## {title}", ""]
        out += [f"> {line}" for line in intro]
        if intro:
            out.append("")
        for row in rows:
            first = md_cell(row[0])
            if title == "Sources":
                out.append(f"- **{first}**: {row[1]}: {row[2]}")
                continue
            out.append(f"### {first}")
            for h, v in zip(header[1:], row[1:]):
                if str(v).strip() and str(v) != "-":
                    out.append(f"- **{h}:** {md_cell(v)}")
            out.append("")
        out.append("")
    os.makedirs(os.path.dirname(MD), exist_ok=True)
    with open(MD, "w") as f:
        f.write("\n".join(out))


def build():
    tabs, values = fill_placeholders(content.TABS)
    rows = stacked_rows(tabs)
    build_xlsx(tabs)
    build_csv(rows)
    build_html(rows)
    build_md(tabs)
    return tabs, rows, values


if __name__ == "__main__":
    _, rows, values = build()
    print("rows in sheet layout:", len(rows), "| placeholders:", values)
    for path in (XLSX, CSV, HTML, MD):
        print(path, os.path.getsize(path), "bytes")
