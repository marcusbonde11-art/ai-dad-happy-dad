# Automated clip pipeline: Drive → Descript → Claude → Review Log (→ Metricool, optional)

Built 2026-10-20 from Prompt Library row 13; wired into Make and reworked on 2026-10-21 (row 13b).
Descript import fixed on 2026-10-22 (URL import instead of direct upload, see "How it works").
Status: **both scenarios ON and verified end to end for step 1** (a 73 MB test recording produced a
Review Log row "1. Uploaded to Descript · transcribing" with a real project ID). No Metricool token
is needed: the Metricool steps are switched off and the pipeline writes everything you need to post
by hand into the Review Log.

## What exists

| Thing | Where | ID |
|---|---|---|
| Drive watch folder **AI Dad Happy Dad - Raw Recordings** (drop recordings here) | https://drive.google.com/drive/folders/1fAVvXFnkZPAaHAP0gFWCHTyyFSLMM_Fa | `1fAVvXFnkZPAaHAP0gFWCHTyyFSLMM_Fa` |
| Drive output folder **AI Dad Happy Dad - Clips (auto)** (finished clips land here, private) | https://drive.google.com/drive/folders/1zXQGPU835CXsu8mKd_k8aut8Slf7a3o8 | `1zXQGPU835CXsu8mKd_k8aut8Slf7a3o8` |
| Google Sheet **AI Dad Clip Pipeline – Review Log** (every step logs a row here) | https://docs.google.com/spreadsheets/d/18oYWSHC-30GD_oGVgJIMp3iKMnys5_y1qGuCHNrl4Yg/edit | `18oYWSHC-30GD_oGVgJIMp3iKMnys5_y1qGuCHNrl4Yg` |
| Make scenario 1 **AI Dad Clips 1/2 – Drive watch → Descript import** (every 15 min) | https://us2.make.com/3002223/scenarios/6717243/edit | `6717243` |
| Make scenario 2 **AI Dad Clips 2/2 – Descript callback → clip → captions → review log (Metricool optional)** | https://us2.make.com/3002223/scenarios/6717242/edit | `6717242` |
| Make webhook **AI Dad Clips – Descript callback** (its URL is already in both CONFIG modules; not written here because this repo is public) | Make → Webhooks | hook `2963382` |
| Make connections | Google Drive `11845960` (Marcus's Google Drive connection (AI Dad clips)); Google Sheets `11391947` | team **My Team** `3002223` |
| Metricool brand `aidadhealthydad` (only used if you switch Metricool on later) | Metricool planner | blogId `6987872`, userId `5392334`, timezone America/New_York |
| Blueprints (clean, placeholder-only copies of both scenarios) | `automation/make/*.blueprint.json` | |

Naming note: the prompt asked for "AI Dad Happy Dad" folder names, so the Drive folders use that.
The channel itself is **AI Dad Healthy Dad** (see CLAUDE.md); the caption prompt uses the Healthy
Dad name. Rename the folders if you like; only the folder IDs matter to Make.

## How it works

```
Phone → Drive "Raw Recordings" folder
   │  (scenario 1, polls every 15 min; everything uploaded in that window runs as one batch)
   ├─ read the file size + extension (metadata only)
   ├─ ≤ 100 MB: link-share the file (anyone with the link, viewer, not searchable)
   │            POST descriptapi.com/v1/jobs/import/project_media (URL import: Descript fetches
   │              https://drive.usercontent.google.com/download?id=<file>&export=download&confirm=t
   │              itself; that URL serves the bytes with HTTP Range support, which Descript needs)
   │            2xx → log row "1. Uploaded to Descript · transcribing"
   │            anything else → log row "1. ERROR – Descript rejected the import" (file is not retried)
   └─ > 100 MB: log row "1. SKIPPED – recording over 100 MB" (needs you), nothing else happens
Descript → calls back scenario 2's webhook when each job finishes
   │  job_type = import/project_media → POST /jobs/agent (Underlord picks the best 20–60 s moment,
   │                        new 9:16 composition "AI Dad Clip", filler words out, Studio Sound,
   │                        captions)                               → log row "2."
   │  job_type = agent   → GET /projects/{id}, pick the "AI Dad Clip" composition (else newest),
   │                        stop if longer than MAX_CLIP_SECONDS, else POST /jobs/publish → log "3."
   │  job_type = publish → export clip transcript (txt)
   │                        download the rendered clip → save to Drive "Clips (auto)" (private)
   │                        Claude (Sonnet 5.5, via Make's AI provider): TikTok + Instagram captions
   │                        METRICOOL_ENABLED = false (default):
   │                           log row "4. READY TO POST – post by hand" with the Drive clip link,
   │                           transcript, both captions and the suggested post times
   │                        METRICOOL_ENABLED = true:
   │                           link-share the clip, schedule TikTok (tomorrow 10:00 ET) and the
   │                           Instagram Reel (day after, 10:00 ET) in Metricool → log "4. REVIEW ME"
   └─ any error         → log row "ERROR", nothing posted
```

Guardrails baked in:
- **Recordings are link-shared as viewer, not searchable, so Descript can fetch them.** Descript's
  URL import needs a URL its servers can reach, and Google Drive has no expiring "anyone" links, so
  scenario 1 turns on "Anyone with the link · Viewer" (file discovery off) right before the import
  call. Nothing passes through Make any more. The Review Log row says it was shared and how to undo
  it; once row 2 ("Transcribed") appears Descript has its own copy and you can remove the link
  sharing in Drive. The finished clip is link-shared only when `METRICOOL_ENABLED` is true.
- **Why not Descript's direct-upload mode (the first build)?** It exists and the payload shape was
  fine; every run was failing with 400 because `folder_name` requires `team_access` ("view",
  "comment" or "edit"). That field is now sent (`team_access: "view"`), and the URL import mode was
  kept because it removes the 100 MB-through-Make limit and the double transfer.
- **Metricool is off by default.** `METRICOOL_ENABLED` in scenario 2's CONFIG is the single switch.
  While it is false, modules 43 and 46–50 never run and nothing is scheduled or published. When you
  pick a Metricool plan: paste `METRICOOL_USER_TOKEN`, set `METRICOOL_ENABLED` to true, save.
  `METRICOOL_AUTO_PUBLISH` stays false even then, so posts wait in the planner for your tap.
- Nothing deletes or moves source recordings. Nothing is pushed to GitHub by the scenarios.
- Captions follow CLAUDE.md: short punchy TikTok, longer Instagram with hashtags, no alcohol or
  specific-habit references, no "you're not broken" framing, no invented facts.

## What is left (Marcus)

1. **Descript API token.** Descript → App settings → API tokens → Create token (pick the Drive that
   holds your projects). Paste it in Make, never into chat or a terminal:
   - Scenario 2 (link above) → click module 2 "CONFIG" → variable `DESCRIPT_API_TOKEN` → replace
     the placeholder → OK → save the scenario.
   - Scenario 1 (link above) → click module 2 "CONFIG" → variable `DESCRIPT_API_TOKEN` → same
     token → OK → save. *(Done 2026-10-22: both tokens are in and both scenarios are on.)*
2. **Scenario order.** Scenario 2 must be on before scenario 1 (webhook scenarios must be on to
   receive callbacks). Both are on today.
3. **Test with one short video (under 100 MB, roughly 60–90 s of 1080p phone footage).** Drop it
   into Raw Recordings. Within 15 minutes the Review Log gets row "1. Uploaded to Descript". Rows
   2, 3 and 4 follow as Descript finishes each job (a few minutes each). Row 4 has the clip link
   (column P), the transcript (I), the Descript share link (J), the TikTok caption (L), the
   Instagram caption (M) and the suggested post times (N, O). Download the clip from the Clips
   (auto) folder and post it by hand. *(Step 1 verified 2026-10-22 with
   "20261020_070757 pipeline-test.mp4", a copy of a real recording: row 1 "ok" with a real project
   ID, then row 2 "Transcribed · clip finding started" (41 s of media) once scenario 2's import
   filter was fixed. Rows 3–4 depend on Descript's later callbacks.)*
4. **Tune.** All knobs live in scenario 2's CONFIG module: posting times and day offsets,
   `MAX_CLIP_SECONDS` (90), `IG_HASHTAG_HINTS` (update from the Sunday doc's caption re-check),
   `CLIP_COMPOSITION_NAME`, `METRICOOL_ENABLED`, `METRICOOL_AUTO_PUBLISH`. Scenario 1's CONFIG
   holds `MAX_UPLOAD_BYTES` (100 000 000, the Make Core limit).

Re-importing a blueprint from `automation/make/` later? Paste the webhook URL (Make → Webhooks →
"AI Dad Clips – Descript callback") into `DESCRIPT_CALLBACK_URL` in both CONFIG modules, and pick
the Google Drive connection in scenario 1 modules 1, 3 and 10 and scenario 2 modules 42 and 43.
Scenario 1's CONFIG also needs `team_access` left as "view" in module 11's body (Descript rejects
`folder_name` without it).

## Posting times (why 10:00 ET)

Pulled from Metricool's best-time-to-post data for brand 6987872 on 2026-10-20 (Oct 21–27, ET).
For both TikTok and Instagram the 10:00 hour scores highest every day of the week, with a second
peak around 18:00. The account is new, so this is Metricool's general curve, not your audience's
yet. The launch plan's "TikTok first, Instagram about 24 h later" rule is kept via the day
offsets. Revisit after ~3 weeks of posting when Metricool has your own data.

| Network | Top hour (ET) | Second peak |
|---|---|---|
| TikTok | 10:00 (Wed/Thu highest) | 18:00 |
| Instagram | 10:00 | 18:00 |

## Limits and things to verify on the first run

- **100 MB per recording.** The limit is now Google's, not Make's: Drive serves a direct download
  only for files it can virus-scan (up to 100 MB); above that the download URL returns a warning
  page instead of the video and Descript cannot import it. At typical phone settings (1080p/30,
  HEVC) 100 MB is roughly 90 seconds to 2 minutes of footage; at 4K it is well under a minute.
  Larger files are logged as "SKIPPED" and left untouched. Options if this bites: film in 1080p,
  trim before uploading, or ask Claude Code to route big files through a host that serves them
  without the interstitial. `MAX_UPLOAD_BYTES` in scenario 1's CONFIG holds the cap.
- **Data transfer.** Raw recordings no longer pass through Make (Descript fetches them from Drive),
  so scenario 1 uses almost no transfer. Scenario 2 still downloads each rendered clip (~30–60 MB)
  to save it in Drive.
- **Underlord creating a new composition.** Descript's docs show prompts like "create a 30-second
  highlight reel" and "add captions" but do not spell out creating a named composition. The
  prompt asks for a new composition called "AI Dad Clip" and falls back to trimming the existing
  one. Scenario 2 picks the composition named "AI Dad Clip", otherwise the newest one, and refuses
  to publish anything longer than `MAX_CLIP_SECONDS`. Check row 3's note on the first run.
- **Rendered clip size.** A 90 s 1080p clip from Descript should stay under 100 MB, but if a
  publish callback ever fails at module 41 ("file too large"), lower `MAX_CLIP_SECONDS`.
- **Make's AI provider.** The caption module uses Make's built-in Claude access (Sonnet 5.5) and
  needs no API key. It bills Make credits, not your Anthropic account.
- **Batching.** "Wait 15 minutes, then batch" is implemented as a 15-minute poll: every file that
  landed in the same window runs in one execution. A file still uploading at poll time is picked
  up next window. Make Core allows a 1-minute minimum, so you can tighten this later.
- **Callback job_type.** Descript reports the import job as `import/project_media` (not `import`).
  Scenario 2's route A accepts both spellings since 2026-10-22; before that the import callback
  matched no route and the pipeline silently stopped after row 1.
- **Descript errors do not retry.** Module 11 never throws; a non-2xx answer is logged as
  "1. ERROR – Descript rejected the import" with Descript's message and the file is considered
  handled (drop it in again to retry). Before this change a failing import re-ran every 15 minutes
  and re-downloaded the file each time.
- **Make usage.** Roughly 25 operations per video across both scenarios, plus 1 per idle poll
  (~96/day, ~2 900/month on a 10 000/month Core plan). Setting scenario 1 to run only 5:00–23:00 ET
  (Scheduling → advanced) cuts that by a quarter.

## Sources used

- Descript API overview, import endpoint (URL and direct-upload modes), direct-upload guide:
  https://help.descript.com/developers · https://help.descript.com/api-and-mcp/api ·
  https://help.descript.com/developers/api-reference/import/import-project-media ·
  https://help.descript.com/developers/guides/direct-upload
- Make file-size limits per plan: https://help.make.com/working-with-files
- Metricool API header, IDs and scheduler endpoint:
  https://help.metricool.com/common-questions-and-errors-when-using-the-api-8x9nq
- Metricool best times: pulled live via the Metricool connector on 2026-10-20.
