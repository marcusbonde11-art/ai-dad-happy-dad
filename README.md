# AI Dad Healthy Dad

Content and coaching for dads with ADHD. **A**I **D**ad **H**ealthy **D**ad = ADHD.
Platforms: TikTok first, then Instagram Reels. First post: Wednesday, Oct 14, 2026.

## What's here

| Path | What it is |
|---|---|
| [`docs/LAUNCH_PLAN.md`](docs/LAUNCH_PLAN.md) | The full plan: name decision, trademark detail, tool stack, timing, trends, 3 first-post scripts, bios, content pillars, assumptions, sources |
| `deliverables/AI_Dad_Launch_Plan.xlsx` | Same plan, one tab per section |
| `deliverables/AI_Dad_Launch_Plan.csv` | Single-tab version (what was uploaded to the project Google Sheet) |
| `tools/content.py` | Source of truth for all plan content |
| `tools/build_workbook.py` | Rebuilds the .xlsx, .csv and Markdown from `content.py` |

The project Google Sheet is **AI Dad Healthy Dad: Launch Plan (Oct 2026)** in the owner's Google Drive.

## Rebuild

```sh
python3 tools/build_workbook.py   # needs openpyxl
```
