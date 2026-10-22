# Clip pipeline: auto-pick the best take from multiple recordings

Built 2026-10-22 from Prompt Library row 24. Extends the pipeline described in [`CLIP_PIPELINE.md`](CLIP_PIPELINE.md).

Make scenarios: **AI Dad Clips 1/2** (id 6717243, Drive watch → Descript import) and **AI Dad Clips 2/2** (id 6717242, Descript callbacks → best take → clip → captions → Review Log).
Review Log sheet: `18oYWSHC-30GD_oGVgJIMp3iKMnys5_y1qGuCHNrl4Yg` (columns Q–U were added for take groups).

`automation/make/*.blueprint.json` are the exact live scenario blueprints with the Descript token and the webhook URL replaced by placeholders (the real values live only in each scenario's CONFIG module). `automation/make/best-take-scoring-prompt.txt` is the scoring prompt verbatim, as it sits in the Claude module of scenario 2/2.

## Tested 2026-10-22

* 4 files dropped together (2 real takes, 1 over 100 MB, 1 corrupt): both exclusions logged with Descript's reason, the two real takes scored 62/62 (identical copies), logged as a 0-point near-tie broken on hook quality then lowest take number, winner sent to Underlord, clip rendered, saved to Drive, captions written, `4. READY TO POST` row logged. No pipeline errors.
* 2 corrupt files dropped together: one `3. ERROR – no take in the group could be transcribed` row, no winner.

## How multiple takes are handled

1. **Grouping (scenario 1/2).** Every video/audio file that the 15-minute Drive poll picks up in the same run is treated as a take of the same piece. If a poll finds 2+ files they get a shared *Take group* key (`G-<date-time>-<id prefix>`), a *Take #* (1..n) and *Takes in group* (n), written to columns Q, R, S of every Review Log row for that recording. One file in a poll = the old single-recording behaviour, unchanged.
   *Practical rule for Marcus: drop all takes of one piece into Raw Recordings together and let the uploads finish within the same 15-minute window. A take that lands in the next window becomes its own single recording.*
2. **Transcription (unchanged).** Each take is imported into its own Descript project exactly as before. When Descript calls back, scenario 2/2 looks up the take's stage-1 row by Descript project ID to learn its group.
3. **Collect transcripts.** For a grouped take, 2/2 exports the full transcript (`POST /v1/export/transcript`, txt) and writes a row `2. Take transcribed · waiting for other takes` (status `waiting`, transcript in column I). A take whose import failed, whose transcript export failed, that was rejected by Descript, or that was over 100 MB gets a `2. Take EXCLUDED – …` row (status `excluded`) instead. After every such row the scenario posts a small `pick_best_take` ping to its own webhook.
4. **Pick (route E of 2/2).** On each ping it counts resolved takes for the group (transcribed + excluded) against *Takes in group*. When the group is complete and nothing has been decided yet:
   * ≥1 transcript → Claude scores every transcribed take (prompt below), the winner's Descript project is sent to Underlord for clip-finding, and one row `3. Best take chosen · clip finding started` (status `ok`) is logged with the one-line reason (column U) and all scores (column T). Excluded takes are named in the Notes.
   * 0 transcripts → one row `3. ERROR – no take in the group could be transcribed` (status `error`), no winner, nothing sent to Underlord.
   Later pings for an already-decided group do nothing. Non-chosen takes are left alone in Drive and in Descript.
5. The winner then flows through the existing clip → publish → captions → Review Log steps.

Scenario 2/2 runs with *sequential processing* on so two pings for the same group cannot both pick.

## Scoring method (grounded; do not change without Marcus)

Grounding: Cooper, Heron & Heward, *Applied Behavior Analysis* 3rd ed., Ch. 29 – self-evaluation is comparing performance "with a predetermined goal or standard" (p. 694) and one should "self-monitor the most important dimension of the target behavior", i.e. the dimension "that … would yield the most direct and significant progress toward [the] goal" (p. 698); and Gary Vaynerchuk's first-3-seconds hook principle plus "if the stuff's good, people find it interesting and valuable, and if the stuff's not good, we put as much polish as we want on it, doesn't matter."

* **Dimension A – Hook/content quality (0–100):** specific, concrete promise in the first 3 seconds (≈ first 8–10 words), delivered on by the rest, message lands clearly.
* **Dimension B – Delivery cleanliness (0–100):** fillers, repeats, restarts, run-ons – judged from the transcript. A stumble inside the first 3 seconds costs ~3× a stumble later (the opening is the dimension that most directly predicts whether the clip is watched).
* **Combined = round(0.65 × A + 0.35 × B)** – hook-weighted, not equal.
* **Tie-break:** top two combined scores within 3 points → decide on Dimension A alone; if still tied, lower take number. The reason line says "near-tie, N points apart, won on hook quality".
* **Reason:** one line naming the deciding dimension, logged to column U and the Notes.

## Failure handling

| Case | What happens |
|---|---|
| One take fails to transcribe (Descript error / partial) | `2. Take EXCLUDED` row, group continues, winner picked from the rest, exclusion named in the pick row |
| One take rejected by Descript at import or over 100 MB | same, logged from scenario 1/2 |
| Every take fails | single `3. ERROR` row (status `error`), no winner |
| Publish callback has no download URL | fallback lookup `GET /v1/published_projects/{slug}`; if still none, `4. READY TO POST – download from Descript by hand` (status `needs you`) with captions |

## Bugs fixed on the way (pre-existing in 2/2)

* Clip download module lacked three required fields and the publish callback carries no `download_url` → added the published-project fallback.
* Drive upload lacked the required `convert` field.
* Transcript export returns a binary buffer; it is now converted to text before writing to Sheets or prompts.
* CONFIG in 1/2 must sit after the batch aggregator (Make cannot read modules that were aggregated away).
