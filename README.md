# AI Dad Healthy Dad

Content and coaching for dads with ADHD. **A**I **D**ad **H**ealthy **D**ad = ADHD.
Platforms: TikTok first, then Instagram Reels. First post: Wednesday, Oct 14, 2026.

## What's here

| Path | What it is |
|---|---|
| [`docs/LAUNCH_PLAN.md`](docs/LAUNCH_PLAN.md) | The full plan: name decision, trademark detail, tool stack, filming logistics, timing, trends, 3 first-post scripts (hooks and beats), bios, 6 content pillars (15 ideas each), assumptions with the re-check log, sources |
| `deliverables/AI_Dad_Launch_Plan.xlsx` | Same plan, one tab per section |
| `deliverables/AI_Dad_Launch_Plan.csv` | Single-tab layout, sections stacked: exactly what's in the project Google Sheet |
| `deliverables/sheet_paste.html` | The same single-tab layout as an HTML table, used to update the Google Sheet in place |
| `tools/content.py` | Source of truth for all plan content |
| `tools/build_workbook.py` | Rebuilds the .xlsx, .csv, .html and Markdown from `content.py` |
| `tools/check_content.py` | Review pass 1: hint words, bio limits, idea counts (6 pillars), hook/beats/closing/tagline/caption structure, cross-references |
| `deliverables/weekly/` | Local copies of the Sunday weekly ideas docs (3 sourced ideas per pillar + 15 taglines) |
| [`docs/CLIP_PIPELINE.md`](docs/CLIP_PIPELINE.md) | Automated clip pipeline (Drive → Descript → Claude → Review Log, Metricool optional): what exists in Make, what is left, limits |
| [`docs/BEST_TAKE_PICKER.md`](docs/BEST_TAKE_PICKER.md) | Multiple takes of one recording: how they are grouped, scored by Claude (hook/content 65 · delivery 35, ABA Ch. 29 + Gary Vee grounding) and the best one picked; failure handling; test results |
| `automation/make/` | Make.com blueprints for the two clip-pipeline scenarios (placeholders only, no tokens or webhook URLs) |
| `automation/make/best-take-scoring-prompt.txt` | The take-scoring prompt verbatim (the Claude module in scenario 2/2) |
| `tools/verify_sheet.py` | Compares a CSV export of the Google Sheet against the source, cell by cell |

The project Google Sheet is **AI Dad Healthy Dad: Launch Plan (Oct 2026)** in the owner's Google Drive.

## Rebuild and check

```sh
python3 tools/build_workbook.py   # needs openpyxl
python3 tools/check_content.py    # exits non-zero on any problem
```
