"""Automated re-check for the launch plan (review pass 1).

Usage: python3 tools/check_content.py
Prints every problem found; exits non-zero if there are any.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
import build_workbook as bw  # noqa: E402
import content  # noqa: E402

problems = []


def problem(msg):
    problems.append(msg)


tabs, values = bw.fill_placeholders(content.TABS)
by_title = {t[0]: t for t in tabs}
rows = bw.stacked_rows(tabs)

# 1. The habit is never named or hinted at.
#    STRICT words name the habit; they're banned everywhere except the name/trademark sections, where
#    facts about the third-party Happy Dad seltzer brand are unavoidable.
#    SOFT words only hint (sobriety slang, day counters, drink-hour times); they're banned in everything
#    that will be said, shown or posted: scripts, bios, pillar ideas and the calendar.
STRICT = [
    r"alcohol", r"\bsober", r"sobriety", r"\bdrink", r"booze", r"\bbeer", r"\bwine", r"liquor", r"hangover",
    r"relapse", r"craving", r"sept(ember)? ?8", r"\b9[./]8\b", r"five weeks", r"\baf\b", r"happy hour",
    r"seltzer", r"\bbottle",
]
SOFT = [
    r"recover", r"\burge", r"trigger", r"\bday \d+", r"friday night", r"\bclean\b", r"\bslip", r"\b5 ?pm\b",
    r"(?<!third-)\bparty\b", r"\bbuzz", r"\bhigh\b", r"\b(a|my|the next) fix\b",
]
PUBLIC_SECTIONS = {"Scripts", "Bio", "Content Pillars", "Week 1 Calendar"}
EXEMPT_SECTIONS = {"Name Decision", "Trademark Detail", "Handles & Domains", "Sources"}
EXEMPT_PHRASES = [
    # Start Here's name-decision summary describes the third-party brand, not the user's story.
    "the Nelk / Full Send hard seltzer", "Class 33 (hard seltzer)",
    # Pillar 5's format word: every 'In the Wild' idea ends with 'Fix: <the practical fix>'.
    "Fix: ",
]
for title, intro, header, body in tabs:
    if title in EXEMPT_SECTIONS:
        continue
    patterns = STRICT + (SOFT if title in PUBLIC_SECTIONS else [])
    for cell in intro + [c for r in body for c in r]:
        text = cell
        for phrase in EXEMPT_PHRASES:
            text = text.replace(phrase, "")
        for pat in patterns:
            m = re.search(pat, text, re.I)
            if m:
                problem(f"[banned] {title}: '{m.group(0)}' in: {cell[:90]}...")

# 2. Bio character limits (counted as the apps do: an emoji counts as 2).
LIMITS = {("TikTok", "Name"): 30, ("TikTok", "Bio"): 80, ("Instagram", "Name"): 64, ("Instagram", "Bio"): 150}
for (platform, field), limit in LIMITS.items():
    n = bw.utf16_len(bw.bio_copy(platform, field))
    if n > limit:
        problem(f"[bio] {platform} {field} is {n} chars, limit {limit}")

# 3. Exactly 15 ideas per pillar, no near-duplicate idea titles across pillars.
ideas = {}
for name in ["PILLAR_1_IDEAS", "PILLAR_2_IDEAS", "PILLAR_3_IDEAS", "PILLAR_4_IDEAS", "PILLAR_5_IDEAS"]:
    lst = getattr(content, name)
    if len(lst) != 15:
        problem(f"[pillars] {name} has {len(lst)} ideas, expected 15")
    for idea in lst:
        key = re.sub(r"[^a-z ]", "", idea.split(":")[0].split(". Save")[0].split(". Fix")[0].lower()).strip()
        if key in ideas:
            problem(f"[pillars] duplicate idea title '{key}' in {name} and {ideas[key]}")
        ideas[key] = name

# 4. Scripts: spoken length 60-75 s at ~2.5 words/s, time ranges in order, every script has a Detail check and CTA.
spoken = {}
for r in by_title["Scripts"][3]:
    script, beat, timing, _, say, _ = r
    spoken.setdefault(script, {"words": 0, "beats": [], "times": []})
    spoken[script]["beats"].append(beat)
    if beat not in ("Post copy", "Detail check"):
        spoken[script]["words"] += len(say.split())
        spoken[script]["times"].append(timing)
for script, info in spoken.items():
    secs = info["words"] / 2.5
    if not 55 <= secs <= 78:
        problem(f"[script] {script}: {info['words']} spoken words ≈ {secs:.0f}s (target 60-75s)")
    if "Detail check" not in info["beats"]:
        problem(f"[script] {script}: no Detail check row")
    if not any("CTA" in b for b in info["beats"]):
        problem(f"[script] {script}: no soft CTA beat")
    ends = [int(t.split("-")[1].rstrip("s")) for t in info["times"]]
    starts = [int(t.split("-")[0]) for t in info["times"]]
    if starts[0] != 0 or any(starts[i + 1] != ends[i] for i in range(len(ends) - 1)):
        problem(f"[script] {script}: time ranges don't chain: {info['times']}")
    if secs and abs(ends[-1] - secs) > 12:
        problem(f"[script] {script}: timeline ends at {ends[-1]}s but spoken length is ≈{secs:.0f}s")

# 5. Placeholders filled; no cell that Sheets would mangle (leading apostrophe/equals/plus).
for r in rows:
    for c in r:
        if re.search(r"\{[A-Z_]+\}", c):
            problem(f"[placeholder] unfilled: {c[:80]}")
        if c[:1] in ("'", "=", "+"):
            problem(f"[sheets] cell starts with {c[:1]!r}: {c[:60]}")

# 6. Cross-references: script names used in Start Here and the calendar exist; sources are https.
script_names = {s.split(": ", 1)[0]: s.split(": ", 1)[1].replace(" (POST FIRST)", "") for s in spoken}
for title in ("Start Here", "Week 1 Calendar"):
    for r in by_title[title][3]:
        for cell in r:
            # "Script B ('The Acronym')" in Start Here, "Script B: 'The Acronym'" in the calendar.
            for letter, quoted in re.findall(r"Script ([ABC])(?::| \() ?'([^']+)'", cell):
                if script_names.get(letter) != quoted:
                    problem(f"[xref] {title} calls Script {letter} '{quoted}', but it's '{script_names.get(letter)}'")
for r in by_title["Sources"][3]:
    if not r[2].startswith("https://"):
        problem(f"[sources] not an https URL: {r[2]}")

# 7. Pillar names match everywhere they're mentioned.
pillar_names = ["5AM Brain", "AI External Brain", "Late-Diagnosis Log", "Pattern Breaks", "ADHD Dad in the Wild"]
for name in pillar_names:
    for title in ("Start Here", "Content Pillars"):
        blob = " ".join(by_title[title][1]) + " ".join(c for r in by_title[title][3] for c in r)
        if name not in blob:
            problem(f"[xref] pillar '{name}' missing from {title}")

print(f"{len(rows)} rows in sheet layout; placeholders {values}")
for script, info in spoken.items():
    print(f"  {script}: {info['words']} spoken words ≈ {info['words'] / 2.5:.0f}s, timeline {info['times'][0]}..{info['times'][-1]}")
for k in LIMITS:
    print(f"  {k[0]} {k[1]}: {bw.utf16_len(bw.bio_copy(*k))}/{LIMITS[k]}")
print(f"{len(problems)} problem(s)")
for p in problems:
    print(" -", p)
sys.exit(1 if problems else 0)
