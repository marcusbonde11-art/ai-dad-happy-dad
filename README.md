# AI Dad Healthy Dad

Content and coaching for dads with ADHD. **A**I **D**ad **H**ealthy **D**ad = ADHD.
Platforms: TikTok first, then Instagram Reels. First post: Wednesday, Oct 14, 2026.

## What's here

| Path | What it is |
|---|---|
| [`docs/LAUNCH_PLAN.md`](docs/LAUNCH_PLAN.md) | The full plan: name decision, trademark detail, tool stack, filming logistics, timing, trends, 3 first-post scripts, bios, content pillars (15 ideas each), assumptions with the re-check log, sources |
| `deliverables/AI_Dad_Launch_Plan.xlsx` | Same plan, one tab per section |
| `deliverables/AI_Dad_Launch_Plan.csv` | Single-tab layout, sections stacked: exactly what's in the project Google Sheet |
| `deliverables/sheet_paste.html` | The same single-tab layout as an HTML table, used to update the Google Sheet in place |
| `tools/content.py` | Source of truth for all plan content |
| `tools/build_workbook.py` | Rebuilds the .xlsx, .csv, .html and Markdown from `content.py` |
| `tools/check_content.py` | Review pass 1: hint words, bio limits, idea counts, script timing, cross-references |
| `tools/verify_sheet.py` | Compares a CSV export of the Google Sheet against the source, cell by cell |

The project Google Sheet is **AI Dad Healthy Dad: Launch Plan (Oct 2026)** in the owner's Google Drive.

## Rebuild and check

```sh
python3 tools/build_workbook.py   # needs openpyxl
python3 tools/check_content.py    # exits non-zero on any problem
```
