"""Compare a Google Sheet CSV export against deliverables/AI_Dad_Launch_Plan.csv, cell by cell.

Usage: python3 tools/verify_sheet.py <export.json | export.csv>
The .json form is what the Drive connector's download tool saves: {"content": "<base64 csv>", ...}.
"""
import base64
import csv
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE = os.path.join(ROOT, "deliverables", "AI_Dad_Launch_Plan.csv")


def load_export(path):
    raw = open(path, encoding="utf-8").read()
    if path.endswith(".json") or raw.lstrip().startswith("{"):
        raw = base64.b64decode(json.loads(raw)["content"]).decode("utf-8")
    return list(csv.reader(io.StringIO(raw)))


def trim(row):
    row = list(row)
    while row and row[-1] == "":
        row.pop()
    return row


def main(path):
    sheet = [trim(r) for r in load_export(path)]
    source = [trim(r) for r in csv.reader(open(SOURCE, encoding="utf-8"))]
    while sheet and not sheet[-1]:
        sheet.pop()
    problems = []
    for i in range(max(len(sheet), len(source))):
        got = sheet[i] if i < len(sheet) else None
        want = source[i] if i < len(source) else None
        if got != want:
            problems.append((i + 1, want, got))
    print(f"sheet rows with content: {len(sheet)} | source rows: {len(source)} | mismatched rows: {len(problems)}")
    for row_no, want, got in problems[:10]:
        print(f"  row {row_no}:\n    want {want}\n    got  {got}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
