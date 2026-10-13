"""Build the launch-plan workbook (.xlsx) and a Markdown copy from content.py.

Usage: python3 tools/build_workbook.py
Outputs: deliverables/AI_Dad_Launch_Plan.xlsx, docs/LAUNCH_PLAN.md
"""
import csv
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill

sys.path.insert(0, os.path.dirname(__file__))
from content import TABS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
XLSX = os.path.join(ROOT, "deliverables", "AI_Dad_Launch_Plan.xlsx")
MD = os.path.join(ROOT, "docs", "LAUNCH_PLAN.md")
CSV = os.path.join(ROOT, "deliverables", "AI_Dad_Launch_Plan.csv")

HEADER_FILL = PatternFill("solid", fgColor="1F2937")
HEADER_FONT = Font(bold=True, color="FFFFFF")
WRAP = Alignment(wrap_text=True, vertical="top")


def col_width(header, rows, i):
    longest = max([len(str(header[i]))] + [min(len(str(r[i])), 400) for r in rows])
    return max(10, min(70, int(longest / 3.2) + 8)) if longest > 30 else max(10, longest + 4)


def build_xlsx():
    wb = Workbook()
    wb.remove(wb.active)
    for title, intro, header, rows in TABS:
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


def md_cell(v):
    return str(v).replace("\n", "<br>")


def build_md():
    out = ["# AI Dad Healthy Dad: Launch Plan", "",
           "Generated from `tools/content.py`. The same content lives in the project Google Sheet.", ""]
    for title, intro, header, rows in TABS:
        out += [f"## {title}", ""]
        out += [f"> {line}" for line in intro]
        if intro:
            out.append("")
        for row in rows:
            first = md_cell(row[0])
            out.append(f"### {first}" if title not in ("Sources",) else f"- **{first}**: {row[1]}: {row[2]}")
            if title == "Sources":
                continue
            for h, v in zip(header[1:], row[1:]):
                if str(v).strip() and str(v) != "-":
                    out.append(f"- **{h}:** {md_cell(v)}")
            out.append("")
        out.append("")
    os.makedirs(os.path.dirname(MD), exist_ok=True)
    with open(MD, "w") as f:
        f.write("\n".join(out))


def build_csv():
    """Single-tab version: every section stacked, for upload as one Google Sheet."""
    with open(CSV, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["AI DAD HEALTHY DAD: LAUNCH PLAN (sections below, in order)"])
        w.writerow(["Sections: " + " · ".join(t[0] for t in TABS)])
        for title, intro, header, rows in TABS:
            w.writerow([])
            w.writerow([f"■ {title.upper()}"])
            for line in intro:
                w.writerow([line])
            w.writerow(header)
            w.writerows(rows)


if __name__ == "__main__":
    build_xlsx()
    build_md()
    build_csv()
    print(CSV, os.path.getsize(CSV), "bytes")
    print(XLSX, os.path.getsize(XLSX), "bytes")
    print(MD, os.path.getsize(MD), "bytes")
