"""All launch-plan content for AI Dad Healthy Dad, as tabs of rows.

Each tab is (title, intro_lines, header, rows). build_workbook.py turns this
into the .xlsx, the single-tab CSV/HTML that becomes the Google Sheet, and
docs/LAUNCH_PLAN.md. "{ROWS}" is replaced at build time with the row count of
the stacked Google Sheet.
Research date: 2026-10-13 (updated the night of Oct 13).
"""

RESEARCH_DATE = "2026-10-13"

# ---------------------------------------------------------------------------
# 1. Start Here
# ---------------------------------------------------------------------------
START_HERE = (
    "Start Here",
    [
        "AI Dad ___ Dad: launch plan. Research done " + RESEARCH_DATE + "; updated the night of Oct 13. First post: Wednesday, Oct 14, 2026, morning.",
        "Read this section first. Every section below has the detail behind it.",
    ],
    ["Topic", "Bottom line"],
    [
        ["WHAT CHANGED TONIGHT",
         "(1) Story corrected everywhere: the account never names the habit. The story is now: the same destructive patterns, "
         "over and over → you finally told your wife something had to change → that was the turning point → ADHD diagnosis and "
         "AI, all inside about a month, about two months ago. (2) All three scripts rewritten for filming at your gym, with "
         "specific details. Each script has a 'Detail check' row so you only say what's true. (3) Pillar 3 is now 'Late-Diagnosis "
         "Log', and every pillar has 15 ready-to-film ideas. (4) Bios sharpened with the trend terms from this sheet. (5) New "
         "'Filming Logistics' section: tripod verdict and the gym-music copyright risk. (6) Re-check log at the end of "
         "Assumptions."],
        ["NAME DECISION",
         "Go with AI DAD HEALTHY DAD. 'AI Dad Happy Dad' contains the whole of HAPPY DAD, a brand owned by Happy Dad, LLC (the "
         "Nelk / Full Send hard seltzer). It has live filings in Class 33 (hard seltzer) and a registration covering Class 25 "
         "(clothing and hats), about 23 filings in all, and it keeps adding new HAPPY ___ marks. It markets to young men on "
         "TikTok and Instagram, the same apps you'll be on. Search 'happy dad' and you get their product, not you. For "
         "'Healthy Dad' I found no live federal trademark, and the full phrase 'AI Dad Healthy Dad' has zero search results. The "
         "acronym still spells A-D-H-D. Re-checked after tonight's story change: the call rests on trademark and search "
         "crowding, and neither changed."],
        ["ACTION BEFORE WED",
         "Tonight: (1) Claim @aidadhealthydad on TikTok and Instagram. Also grab @aidadhappydad as a free defensive hold, "
         "but don't post on it. (2) Register aidadhealthydad.com at any registrar, about $10-20/yr. (3) Run the 5 USPTO "
         "queries in the 'Trademark Detail' section yourself; this sandbox's network blocked tmsearch.uspto.gov. (4) Connect "
         "TikTok and Instagram to your Metricool brand. It's linked, but no social accounts are connected yet. (5) Pack the "
         "filming kit and read each script's Detail check row (see Filming Logistics)."],
        ["FILMING AT THE GYM",
         "Talk where the music isn't. Gym speakers play licensed music, your mic will pick it up, and TikTok and Instagram "
         "scan audio automatically. A muted talking video is a dead video. So: record talking parts in your car in the gym lot "
         "or a music-free corner, and use the gym floor for silent B-roll. Turn on TikTok's 'Music copyright check' on the "
         "posting page. A $20-40 tripod with a Bluetooth remote is worth buying."],
        ["POSTING STACK (phone-only)",
         "Write/tighten scripts in the Claude app → film at your gym on a $20-40 tripod with a noise-cancelling clip mic "
         "(DJI Mic Mini class, ~$79 on sale) → edit + auto-captions in CapCut (TikTok master) → re-caption/finish the "
         "Instagram version in Edits (Instagram's free editor, no watermark) → schedule/auto-publish both through Metricool "
         "(already connected) → check TikTok Creative Center and your own For You page 10 min a day for trends. No AI faces, "
         "AI voices, or AI eye-contact fixes. Raw stays raw."],
        ["SEQUENCE",
         "TikTok first, every time. Repurpose to Instagram Reels about 24 hours later with a clean export (no TikTok "
         "watermark) and fresh captions. TikTok's For You feed ranks on content signals, not follower count, so a "
         "zero-follower account can reach people on day one. Instagram rewards originality and 'sends' (shares by DM), so "
         "post a native, clean upload rather than a repost."],
        ["TIMING",
         "First post (Wed): TikTok at 7:30 AM ET, which leaves 45 minutes after the gym to edit and proof captions. From Thursday: "
         "TikTok at 7:00 AM ET, Instagram Reels the next morning at 8:00 AM ET (in line with Hootsuite's morning window and "
         "Hopper's 7-8 AM Reels finding). Week 3: test one evening slot (6-8 PM, Metricool's TikTok study). After about 3 weeks "
         "of posts, switch to Metricool's personalized 'Best times' for your own audience."],
        ["FIRST POST",
         "Post Script B ('The Acronym') first: it has the strongest 1-second hook and explains the channel. Post Script C "
         "('5:40 AM') second and Script A ('The Parking Lot') third. Film all three Wednesday morning, and pin all three on "
         "TikTok (it allows 3 pinned videos). Captions are burned into every video."],
        ["CONTENT PILLARS",
         "1) 5AM Brain: early mornings at the gym as ADHD regulation, not hustle. 2) AI External Brain: real prompts, real "
         "screens. 3) Late-Diagnosis Log: two months in, what the diagnosis changed and didn't. 4) Pattern Breaks: the loop, the "
         "sentence to your wife, repair. 5) ADHD Dad in the Wild: dry humor with one fix. 15 ideas each = 75 videos, about 15 "
         "weeks at 5 a week. Each video gives viewers one thing worth saving."],
        ["WHAT I COULDN'T VERIFY",
         "The sandbox only allows web search, so I couldn't directly query USPTO, domain registries, or TikTok/Instagram "
         "profile pages. Trademark findings come from indexed USPTO-data mirrors (Justia, Trademarkia, uspto.report, "
         "TTABVUE). Handle and domain status is 'no existing use found', not 'confirmed available'. Instagram reach penalties "
         "for muted audio come from third-party guides; Meta hasn't confirmed them. None of this is legal advice. Before you "
         "file a federal application, get a 1-hour clearance review from a trademark attorney."],
    ],
)

# ---------------------------------------------------------------------------
# 2. Name Decision
# ---------------------------------------------------------------------------
NAME_DECISION = (
    "Name Decision",
    ["Criteria in your priority order: trademark → domain → social handles → search crowding. Then brand fit."],
    ["Priority", "Criterion", "AI Dad Happy Dad", "AI Dad Healthy Dad", "Edge"],
    [
        ["1", "Federal trademark conflict",
         "HIGH-MODERATE RISK. HAPPY DAD (SN 90229564, Cl 33 hard seltzer) plus HAPPY DAD HARD SELTZER (SN 90573863, "
         "includes Cl 25 clothing/hats, shown as registered Sep 2, 2025). Owner Happy Dad, LLC has about 23 filings and keeps "
         "extending the name (HAPPY MOM, HAPPY DOG, BABY DADDY, STEP DADDY). Your name contains their whole mark. Coaching "
         "and videos (Class 41) aren't the same goods as seltzer, so an outright refusal isn't certain. But the owner is a "
         "well-funded creator-led brand on your exact platforms with your audience, and any merch you sell would collide "
         "with their Class 25 registration.",
         "LOW RISK. No live HEALTHY DAD federal record found in indexed USPTO mirrors. Similar uses are descriptive: "
         "thehealthydad.com (blog), 'Healthy Dad Convos' (podcast), 'Healthy Dads, Healthy Kids' (university research "
         "program). None is an enforcing brand owner. Caveat: 'healthy' is descriptive, so your protection comes from the "
         "whole phrase, not 'Healthy Dad' alone.",
         "Healthy"],
        ["1a", "Is the 'Happy Dad' hard seltzer a REAL conflict for your account?",
         "Yes, as a real-world conflict, though not a slam-dunk legal loss. Trademark law compares marks, goods and trade "
         "channels, not your message, so your story doesn't move the legal risk either way. On the brand side: #happydad is "
         "seltzer content, people may assume a parody or an affiliate deal, and an account about breaking destructive "
         "patterns would spend its first videos explaining that it isn't a drinks brand.",
         "No drinks-brand association. 'Healthy' fits a story about breaking patterns, early mornings and the gym.",
         "Healthy"],
        ["2", "Domain",
         "aidadhappydad.com: no live site found in search (likely unregistered; verify at a registrar).",
         "aidadhealthydad.com: no live site found in search (likely unregistered; verify at a registrar).",
         "Tie"],
        ["3", "Social handles (TikTok + IG)",
         "@aidadhappydad: no existing account found in indexed results. 14 characters.",
         "@aidadhealthydad: no existing account found in indexed results. 16 characters, within limits (TikTok 24, IG 30).",
         "Tie (Happy is 2 chars shorter)"],
        ["4", "Search crowding",
         "HIGH for 'happy dad'. The brand, retailers, news and 12-pack listings dominate results. The full phrase "
         "'ai dad happy dad' has zero results, but platform search and autocomplete will keep pulling people toward the "
         "seltzer.",
         "MEDIUM for 'healthy dad'. Scattered small blogs and podcasts, no dominant brand. The full phrase 'ai dad healthy "
         "dad' has zero results.",
         "Healthy"],
        ["5", "Brand fit (ADHD + AI + breaking patterns + dry humor)",
         "The word 'Happy' is warmer and funnier, and it reads like a dad joke. But it's someone else's product name.",
         "The word 'Healthy' fits the breaking-patterns, early-gym story. It's a bit earnest, so the dry humor in the content "
         "has to carry the voice.",
         "Slight Happy"],
        ["6", "ADHD acronym works?", "A-D-H-D ✓", "A-D-H-D ✓", "Tie"],
        ["", "RECOMMENDATION",
         "Don't build on it. If you love it, at most hold the handle defensively.",
         "LAUNCH WITH THIS. Claim handles and the domain tonight. Get an attorney's clearance opinion before you file in "
         "Class 41 (education/entertainment/coaching) and, if you plan merch, Class 25.",
         "AI DAD HEALTHY DAD"],
    ],
)

# ---------------------------------------------------------------------------
# 3. Trademark Detail
# ---------------------------------------------------------------------------
TRADEMARK = (
    "Trademark Detail",
    [
        "Method: tmsearch.uspto.gov, Justia and Trademarkia were all blocked by this sandbox's network policy. Results below come "
        "from web-indexed USPTO-data mirrors and TTABVUE, found through search on " + RESEARCH_DATE + ". Statuses can lag, so "
        "confirm each serial number on TSDR (tsdr.uspto.gov).",
        "Run these yourself at tmsearch.uspto.gov (about 5 minutes), filtered to LIVE: CM:\"happy dad\" · CM:\"healthy dad\" · "
        "CM:\"ai dad\" · CM:\"adhd dad\" · CM:\"healthy dad*\". Also search Class 041 and 025 with *dad* to see the field.",
    ],
    ["Mark", "Serial #", "Owner", "Classes / goods", "Status (as indexed)", "Why it matters to you", "Source"],
    [
        ["HAPPY DAD", "90229564", "Happy Dad, LLC (original applicant Nelk Inc.)", "Cl 33: alcoholic beverages, namely hard seltzer",
         "Notice of Allowance issued (Justia). Verify current status on TSDR.",
         "Core mark. Your name contains it whole.", "https://trademarks.justia.com/902/29/happy-90229564.html"],
        ["HAPPY DAD HARD SELTZER", "90573863", "Happy Dad, LLC", "Includes Cl 25 clothing (shirts, sweatshirts, hats, caps) plus other merch",
         "Trademarkia: registered Sep 2, 2025. Justia shows an older non-final action, so the sources conflict. Verify on TSDR.",
         "Blocks AI Dad Happy Dad merch. This is where you'd be most likely to get a refusal or a cease-and-desist letter.",
         "https://www.trademarkia.com/happy-dad-hard-seltzer-90573863"],
        ["HAPPY DAD HARD SELTZER (design)", "90980249", "Happy Dad, LLC", "Multi-class incl. Cl 14 (key chains etc.) and hard seltzer",
         "Approved for publication (Aug 2023 per Justia)", "Shows merch and brand-extension intent.",
         "https://trademarks.justia.com/909/80/happy-dad-hard-90980249.html"],
        ["HAPPY DAD HARD SELTZER MOM", "98248506 / 98366229", "Happy Dad, LLC", "Cl 33 hard seltzer; seltzer/sparkling water",
         "Opposed by We Are Happy, LLC (Opp. No. 91295385, filed 11/26/2024, terminated 3/19/2026; outcome not shown)",
         "The owner fights in TTAB proceedings and keeps filing. It's an active, litigating brand.",
         "https://ttabvue.uspto.gov/ttabvue/v?pno=91295385&pty=OPP"],
        ["Happy Dad, LLC portfolio", "~23 filings", "Happy Dad, LLC", "HAPPY MOM, HAPPY DOG, BABY DADDY, STEP DADDY, STEP MOMMY…",
         "Mixed", "They're building a 'family' of names. Expect them to police anything that looks like HAPPY + family word.",
         "https://trademarks.justia.com/owners/happy-dad-llc-4737642"],
        ["HEALTHY DAD", "None found", "-", "-", "No live federal record found in indexed mirrors",
         "Clears the first pass. Confirm with CM:\"healthy dad\".", "Web search, " + RESEARCH_DATE],
        ["Healthy Dads, Healthy Kids", "None found", "Univ. of Newcastle (AU); US adaptation by Baylor College of Medicine",
         "Research/health program", "No trademark record surfaced",
         "Descriptive coexisting use. Low risk; mention it if an attorney asks about prior uses.",
         "https://www.newcastle.edu.au/research/research-impact/healthy-dads-healthy-kids"],
        ["AI DAD", "None found", "-", "-", "No record found",
         "Clear. Nearby common-law use: 'AI Daddy' (aidaddy.com), a business AI consultancy with different services.",
         "https://www.linkedin.com/in/lucapetty/"],
        ["ADHD DAD", "None found", "-", "-", "No record found", "Clear in federal records. Common-law hashtag use is everywhere and descriptive.",
         "Web search, " + RESEARCH_DATE],
        ["COACH DAD / POSITIVELY DAD / THE DAD'S GROUP CHAT PODCAST", "98172423 / 90007646 / 90031850", "Various",
         "Cl 41 coaching and podcasts; Cl 9 downloadable podcasts", "Mixed (applications/registrations)",
         "Many 'DAD + word' marks coexist in Class 41, so 'DAD' by itself is weak. Your distinctiveness comes from the whole phrase.",
         "https://trademark.justia.com/981/72/coach-98172423.html"],
        ["EARLY DAD (your check)", "None found", "-", "-",
         "No creator, brand, podcast, account or trademark called 'Early Dad' / 'Early Dads' / 'Early Dad Club' found in 4 searches",
         "No conflict found. If you want 'Early Dad' as a series name, search it in the TikTok/IG apps first. The pillar here is "
         "named '5AM Brain' to sidestep it anyway.", "Web search, " + RESEARCH_DATE],
        ["Filing note", "-", "-", "Class 41 (education/entertainment/coaching/videos); Cl 25 only if merch",
         "USPTO base fee: $350 per class (2025 fee schedule; verify)",
         "File after an attorney's knockout/clearance review. With a 1(b) intent-to-use basis you can file before you have revenue.",
         "https://www.uspto.gov/trademarks/search"],
    ],
)

# ---------------------------------------------------------------------------
# 4. Handles & Domains
# ---------------------------------------------------------------------------
HANDLES = (
    "Handles & Domains",
    ["A result of 'not found' means no existing account or site showed up in web-indexed results. These weren't checked live (the sandbox "
     "blocks tiktok.com, instagram.com and registry lookups). Claim them in the apps tonight. That takes 2 minutes and settles it."],
    ["Name", "Asset", "Platform", "Result", "Fallback if taken", "Action"],
    [
        ["AI Dad Healthy Dad", "@aidadhealthydad", "TikTok", "No existing account found", "@aidad.healthydad / @aidadhealthydad_", "CLAIM TONIGHT (primary)"],
        ["AI Dad Healthy Dad", "@aidadhealthydad", "Instagram", "No existing account found", "@aidad.healthydad / @aidadhealthydad_", "CLAIM TONIGHT (primary)"],
        ["AI Dad Healthy Dad", "aidadhealthydad.com", "Domain", "No live site found", "aidadhealthydad.co / getaidad.com", "REGISTER TONIGHT"],
        ["AI Dad Happy Dad", "@aidadhappydad", "TikTok", "No existing account found", "-", "Optional defensive hold (don't post)"],
        ["AI Dad Happy Dad", "@aidadhappydad", "Instagram", "No existing account found", "-", "Optional defensive hold (don't post)"],
        ["AI Dad Happy Dad", "aidadhappydad.com", "Domain", "No live site found", "-", "Skip unless you want to stop squatters"],
        ["Search: 'happy dad'", "-", "Google/TikTok/IG", "Dominated by Happy Dad Hard Seltzer", "-", "Crowding: HIGH"],
        ["Search: 'healthy dad'", "-", "Google/TikTok/IG", "Small blogs and podcasts (thehealthydad.com, Healthy Dad Convos)", "-", "Crowding: MEDIUM"],
        ["Search: full phrases", "-", "Google", "Zero results for both 'AI Dad Happy Dad' and 'AI Dad Healthy Dad'", "-", "Open field"],
    ],
)

# ---------------------------------------------------------------------------
# 5. Alternatives
# ---------------------------------------------------------------------------
ALTERNATIVES = (
    "Alternatives",
    ["Only one of the two names had a real problem, so you don't need these. I checked three backups anyway, in case a handle "
     "turns out to be taken. Each keeps AI + Dad + the A-D-H-D acronym."],
    ["Name", "Trademark", "Domain / handles", "Search crowding", "Verdict"],
    [
        ["AI Dad Hopeful Dad", "No 'Hopeful Dad' record found. Nearest: THE HOPEFUL MAMA (SN 98500313, pending, parenting podcasts), a different mark.",
         "Nothing found for aidadhopefuldad", "LOW: no brand, podcast or account found", "Best backup. Clean, and fits the turning-point story."],
        ["AI Dad Honest Dad", "No federal record found",
         "Nothing found for the full phrase", "HIGH: UK blogger @thehonestdad (IG/X), 'The Honest Dad Co.' podcast, honestdad.blog",
         "Usable but crowded."],
        ["AI Dad Human Dad", "No federal record found, but there's a real common-law brand",
         "Nothing found for the full phrase", "CONFLICT: Human Dad is a fatherhood apparel brand (humandad.com, @humandadbrand) with a paid 'Human Dad Club' community",
         "Avoid: same audience, and it sells merch and community."],
    ],
)

# ---------------------------------------------------------------------------
# 6. Tool Stack
# ---------------------------------------------------------------------------
TOOLS = (
    "Tool Stack",
    ["Everything runs on a phone except the optional TikTok Creative Center check, which also works in a phone browser. "
     "On-camera content stays raw: no AI avatars, AI voices, AI eye-contact correction or AI 'enhance'."],
    ["Job", "Tool (pick)", "Cost", "Why this one", "Watch-outs", "Backup"],
    [
        ["Script writing", "Claude app (+ this sheet as your script bank)", "Free / Pro",
         "Turn a voice-memo brain dump into a hook plus 3 beats. Ask it for 10 hook variants and pick 1. The stories stay yours.",
         "Don't let it write your voice. Read every line aloud, and cut anything you wouldn't say to a friend.", "Apple Notes / Google Keep"],
        ["Teleprompter", "PromptSmart (voice-tracking scroll), for the car shots", "~$9.99/mo",
         "Scrolls only while you talk and pauses when you pause. Works on a dash-mounted phone for Script A.",
         "On the gym floor a teleprompter is awkward and reading kills the raw feel. Use the script's On-screen TEXT lines as "
         "your cue card instead.", "BIGVU free (watermark) / Teleprompter for Video (free short scripts)"],
        ["Record", "Phone's native camera, rear lens, 1080p/30 or 4K/30, on a tripod (see Filming Logistics)", "Free",
         "Best quality you've got. Face the brightest light in the gym; overhead lighting alone flattens faces.",
         "Audio matters more than video: a noise-cancelling wireless clip mic (DJI Mic Mini kit, ~$79 on sale) is the one "
         "purchase worth making. Gym music is a copyright risk; see Filming Logistics.", "-"],
        ["Edit + captions (TikTok master)", "CapCut", "Free (Pro ~$19.99/mo)",
         "Strongest free phone editor. Auto-captions in 55+ languages, jump cuts, text overlays. The 'Reduce noise' toggle and "
         "'Vocal isolation' (Pro) help strip leftover gym music.",
         "Proofread auto-captions: TikTok reads on-screen text and speech to decide what the video is about, so a wrong word can "
         "mis-file it. Pro assets add a watermark on free exports.", "-"],
        ["Instagram version", "Edits (by Instagram)", "Free",
         "No watermark, built for Reels, Instagram-native trending audio, built-in Reel insights, and an audio-enhancement "
         "tool that reduces background noise (per its store listing).",
         "Needs an Instagram login. Re-export from the clean CapCut file, never from a downloaded TikTok (watermarks get "
         "suppressed). One creator reported the audio enhancement glitching at cuts, so listen before posting.",
         "CapCut export without watermark"],
        ["AVOID for this brand", "Captions app's AI features (eye contact, AI avatars, AI dubbing)", "-",
         "You said raw and real. These tools fake exactly that.", "Captions' plain auto-captions are fine. Its 'AI eye contact' is not.", "-"],
        ["Schedule + auto-publish", "Metricool (already connected)", "Free tier (third-party report: ~50 posts/mo; verify)",
         "Schedules and auto-publishes TikTok videos and Instagram Reels. Its 'Best times' feature personalizes to your "
         "audience once you have posting history. I can schedule posts for you through the Metricool connector after "
         "networks are connected.",
         "Your Metricool brand (ID 6987872) has NO social networks connected yet, so connect TikTok and Instagram first. "
         "Instagram must be a Professional (Creator) account. Custom TikTok thumbnails need a TikTok Business account, but "
         "Business accounts lose most commercial music, so stay on a personal/creator account for now.",
         "TikTok and Instagram in-app scheduling"],
        ["Trend awareness", "TikTok Creative Center (trending hashtags, songs, creators) + your own For You page",
         "Free", "Official TikTok data, filterable by region and 7 days.",
         "Trends die in 1-2 weeks. Only use ones you can tie to an ADHD-dad point.",
         "Edits app 'trending audio' tab; Metricool competitor tracking (IG)"],
        ["Analytics", "TikTok Studio + Instagram Insights, rolled up in Metricool", "Free",
         "Watch: average watch time, % watched to the end, saves, shares/sends, follows per video.",
         "Don't judge a video before 72 hours. TikTok often pushes late.", "-"],
        ["Optional automation (later)", "Make (connected)", "Free tier",
         "Week 4+: mark a script row 'Filmed' and auto-create a Metricool draft or a calendar block. (Make is also how this "
         "sheet was updated in place tonight.)", "Not needed for launch. Don't spend Tuesday night on it.", "-"],
    ],
)

# ---------------------------------------------------------------------------
# 7. Filming Logistics (new Oct 13)
# ---------------------------------------------------------------------------
FILMING = (
    "Filming Logistics",
    ["You film at your gym in the morning. Two things decide whether that works: a stable phone, and keeping the gym's "
     "music out of your audio. Researched the night of Oct 13; product claims from vendors are marked as marketing."],
    ["Topic", "Recommendation", "Why / evidence", "Cost", "Source"],
    [
        ["Tripod or stand: worth it?",
         "YES. Buy a tall telescoping phone tripod with a Bluetooth remote: $20-40, and the biggest upgrade after the mic. "
         "Most-cited pick in 2026 gym reviews: the EUCOS 62-in with remote.",
         "Handheld at the gym means arm-length framing, shake, a sweaty grip, and no hands free for B-roll of your lifts. A "
         "tripod lets you set the shot once and just talk. Reviewers rate the EUCOS remote as reliable at ~33 ft but its "
         "plastic build as less premium; the TONEOF 68-in is the sturdier aluminum option. Metric Coach's ~$20 pick held up "
         "to a year of daily use.",
         "$20-40",
         "metric.coach/articles/best-gym-tripod-for-phones · kingswaygym.com/gym-tripod · musclemadnesshq.com/best-gym-tripods"],
        ["Magnetic gym mount (optional add-on)",
         "Only if you want lifting B-roll from the rack: a MagSafe magnetic mount that sticks to steel equipment.",
         "Holds on steel/iron racks and benches, not aluminum. Android phones need the metal ring adapter. Hold-strength "
         "claims (one vendor says 'through a 405 lb deadlift') are marketing; I found no neutral long-term tests.",
         "$25-60",
         "blaubeck.com (vendor) · SmallRig 5460 listing · Amazon listing"],
        ["Skip for now",
         "Gimbals, ring lights, auto-tracking mounts.",
         "Talking-head videos don't move, and raw is the brand. Spend the money on the mic.",
         "$0", "-"],
        ["Shot setup (2 minutes)",
         "Phone vertical, lens at eye level, 3-4 ft away, chest-up framing. Face the brightest light. Back to a wall or corner, "
         "never a mirror.",
         "A wall behind you means no other members and no reflections in frame, which is the #1 gym-filming rule (see the "
         "etiquette row). An eye-level lens reads as a conversation, not a lecture.",
         "-", "Gym filming policies (Axios; Health Club Management)"],
        ["Mic",
         "Wireless clip-on mic with noise cancellation ON, clipped 6-8 in below your chin. DJI Mic Mini class.",
         "A close mic makes your voice much louder than the room. The Mic Mini has two noise-cancellation levels (helps in "
         "moderate noise, not extreme, per New Atlas); the Mic Mini 2S adds AI noise reduction and an internal backup "
         "recording (TechRadar). Neither was tested against gym music, so test yours on your first morning.",
         "~$79 Mic Mini kit on sale ($169 at launch) · ~$88-168 Mini 2S",
         "New Atlas · TechRadar · Kotaku"],
        ["THE MUSIC RISK (read this)",
         "Treat gym music as a real risk. It's highest for talking-to-camera segments.",
         "Gym speakers play licensed music, and your mic will pick it up even at low volume. TikTok: copyrighted music caught "
         "by a mic can get a video's sound muted or removed, and TikTok's Creator Academy describes a 'Music copyright check' on "
         "the posting page that warns you before you publish. Instagram: its help center says reel audio can be muted when "
         "music-rights agreements change, and 2026 guides report automatic detection of copyrighted tracks, muted Reels "
         "getting reduced distribution, and business accounts getting a narrower music library (third-party, not confirmed "
         "by Meta). A muted talking video loses the only thing it has: your voice.",
         "-",
         "TikTok Creator Academy · Instagram Help · LastPlayDistro · InspireToThrive"],
        ["Avoid it #1: talk where there's no music",
         "Record talking segments in your car in the gym lot (Script A is written for this), outside the entrance, in a "
         "stairwell, or in a studio room with the speaker off.",
         "No music in the recording means no copyright match. The car is also the quietest, most private room you have at "
         "5:30 AM.",
         "$0", "-"],
        ["Avoid it #2: voiceover over silent B-roll",
         "On the floor, film B-roll only: chalk, the bar loading, the clock, the empty gym. In CapCut set that audio to 0. "
         "Record your lines in the car and lay them over.",
         "The gym's music never reaches the final file. This is how Scripts B and C cover their gym shots.",
         "$0", "-"],
        ["Reduce it #3: if you must talk on the floor",
         "Mic clipped close with noise cancellation on, stand as far from the speakers as you can, film when the floor is "
         "emptiest, and ask the front desk once whether they'd drop the volume for two minutes.",
         "This lowers the music relative to your voice but rarely removes it, so always check in post (next row).",
         "$0", "-"],
        ["Clean it in post",
         "CapCut: the 'Reduce noise' toggle, then 'Vocal isolation' (a Pro feature, per 2026 tutorials). Edits: 'audio enhancement'. "
         "Then listen on headphones: if you can still hear a melody or lyrics, re-record. Don't post it.",
         "Isolation results depend on the recording (CapCut guide, Aug 2026), and one creator reported Edits' enhancement "
         "glitching at cuts. Your ears are the final check.",
         "Free · CapCut Pro ~$19.99/mo",
         "capcutguide.com · creator tutorial (TikTok) · Edits App Store listing · Threads report"],
        ["Check before and after posting",
         "TikTok: switch on 'Music copyright check' on the posting page (TikTok Studio app or web). Instagram: open the Reel "
         "10 minutes after posting and look for an 'audio unavailable' notice.",
         "If a talking video gets muted anyway, swapping in new audio won't save it, because your voice goes too. Re-record "
         "the voice in the car, rebuild the edit, and post it as a new video. Don't repost the same file: a 2026 guide says "
         "it usually gets muted again.",
         "$0", "TikTok Creator Academy · InspireToThrive"],
        ["Don't fight music with music",
         "Never add a trending song to 'cover' gym music. If you want music, add it from the app's own library at low "
         "volume, after the gym audio is gone.",
         "In-app library sounds are cleared for that platform; a second song doesn't erase the first. Business accounts get a "
         "smaller library (third-party guides), which is another reason to stay on a personal/creator TikTok for now.",
         "$0", "Fox Music · LastPlayDistro"],
        ["Gym etiquette and rules",
         "Ask the front desk once: 'I film short talking videos for my own account. Anywhere you'd rather I didn't?' Never show "
         "another member recognizably, including in mirrors or their voice. Blur anyone who wanders into frame.",
         "Big chains (Life Time, Equinox, Crunch) reportedly ban filming members without permission, and one operator's code "
         "of conduct bars any recognizable person in posts, reflections and audio included. Getting banned from your filming "
         "location would cost more than any video.",
         "$0", "Axios (2025) · Health Club Management · STV News"],
        ["Car setup (Script A)",
         "Phone on a dash or vent mount, or the tripod on the passenger seat. Engine off, windows up, lens at eye level. Sit "
         "back so your shoulders are in frame.",
         "Engine off beats any filter. If it's still dark, park under a lot light or angle your face toward the gym's "
         "entrance lights.",
         "$0-15 (mount)", "-"],
        ["Night-before kit (2 minutes)",
         "Tripod + remote, mic charged, phone at 80%+ with storage cleared. Read each script's Detail check row, then use its "
         "On-screen TEXT lines as your cue card.",
         "No decisions at 5:30 AM. That's the whole point of the 5AM pillar.",
         "-", "-"],
    ],
)

# ---------------------------------------------------------------------------
# 8. Timing & Sequence
# ---------------------------------------------------------------------------
TIMING = (
    "Timing & Sequence",
    ["Times are US Eastern (assumed; see Assumptions). Published studies disagree, so these are starting defaults, not "
     "rules. After about 3 weeks, switch to Metricool's personalized Best Times for your own audience."],
    ["Platform", "Default slot", "Evidence", "Why for you"],
    [
        ["TikTok (post FIRST)", "7:00 AM weekdays (first post: 7:30 AM); test 6-8 PM in week 3",
         "Hootsuite (secondhand): Thu 6-9 AM. Sprout (~2B engagements): Tue-Thu 2-6 PM. Buffer (7.1M posts): Sun 9 AM. Metricool 2026: 6-8 PM.",
         "Studies disagree, so the morning slot matches the brand: you post at the hour you talk about. TikTok judges new "
         "accounts on content, not followers, so timing matters less than the hook."],
        ["Instagram Reels (repurpose ~24h later)", "8:00 AM weekdays",
         "SocialPilot (~250K Reels): 8 AM-12 PM Mon-Thu. Hopper: Tue/Wed 7-8 AM. Buffer: Wed 12 PM, Thu 9 AM.",
         "Morning is the most consistent finding across studies. Instagram leans on followers more, so let TikTok test the "
         "hook first, then post the version that worked."],
        ["Instagram carousel (saveable)", "Sat 9:00 AM",
         "Saves feed Explore ranking (Buffer/Mosseri summaries)", "Turn each week's best tip into a 5-7 slide checklist people save."],
    ],
)

WEEK1 = (
    "Week 1 Calendar",
    ["TikTok first, Instagram next day. Reply to every comment within the first 60 minutes of each post. Launch week runs "
     "the three intro scripts Wed-Fri; the weekly rhythm in Content Pillars starts Monday."],
    ["Date", "Time (ET)", "Platform", "Post", "Pillar", "Notes"],
    [
        ["Tue Oct 13", "Evening", "-", "Claim handles + domain, connect Metricool, set bios, pack the filming kit", "-",
         "Read each script's Detail check row tonight and swap anything that isn't true for you."],
        ["Wed Oct 14", "5:30-6:45 AM ET", "-", "Film at the gym: Script A in the car first, then B and C (talking parts in a music-free spot, B-roll on the floor)", "-",
         "Film all three now; post only B today."],
        ["Wed Oct 14", "7:30 AM ET", "TikTok", "Script B: 'The Acronym'", "Intro",
         "Moved from 7:00 to leave 45 min to edit and proof captions. Post natively in the TikTok app with 'Music copyright check' on; reply for the first hour. Pin it."],
        ["Thu Oct 15", "7:00 AM ET", "TikTok", "Script C: '5:40 AM'", "5AM Brain", "Pin it."],
        ["Thu Oct 15", "8:00 AM ET", "Instagram Reel", "Script B (watermark-free export, Edits captions)", "Intro", "Via Metricool, or in-app if not connected yet"],
        ["Fri Oct 16", "7:00 AM ET", "TikTok", "Script A: 'The Parking Lot'", "Pattern Breaks", "Pin it."],
        ["Fri Oct 16", "8:00 AM ET", "Instagram Reel", "Script C", "5AM Brain", "Metricool"],
        ["Sat Oct 17", "7:00 AM ET", "TikTok", "Reply-to-comment video (best question from Wed-Fri)", "Comment Answers", "TikTok's 'reply with video' button"],
        ["Sat Oct 17", "8:00 AM ET", "Instagram Reel", "Script A", "Pattern Breaks", "Metricool"],
        ["Sat Oct 17", "9:00 AM ET", "Instagram carousel", "Carousel: 'The 3 calls I make between sets' (from Script C)", "5AM Brain", "Saveable checklist"],
        ["Sun Oct 18", "-", "-", "Batch-film 3-4 videos for next week (pick from the 15-idea lists in Content Pillars)", "-", "Morning gym session, 45 min"],
        ["Mon Oct 19", "7:00 AM ET", "TikTok", "AI External Brain #1: 'The prompt I use when I can't start anything'", "AI External Brain", "Put the prompt in the caption so people can copy it"],
        ["Tue Oct 20", "7:00 AM ET", "TikTok", "Pattern Breaks: 'Apologies with an action attached'", "Pattern Breaks", "Put the formula on screen; it's the saveable part"],
    ],
)

# ---------------------------------------------------------------------------
# 9. Trends
# ---------------------------------------------------------------------------
TRENDS = (
    "Trends (Oct 2026)",
    ["What's moving now in dad, parenting and ADHD content, and how to use it without becoming a trend account."],
    ["Trend / signal", "Platform", "Evidence", "How AI Dad uses it", "Shelf life"],
    [
        ["Late-diagnosed / undiagnosed ADHD dads", "TikTok", "TikTok search cluster 'dad undiagnosed adhd' is active. Few established creators combine ADHD + dad, so the niche is open.",
         "That's your story exactly, and now its own pillar (Late-Diagnosis Log). Say 'late-diagnosed' and 'ADHD dad' out loud "
         "early; they're the search terms.", "Evergreen"],
        ["Backlash against ADHD misinformation", "TikTok, IG",
         "UEA study (Mar 2026): ~52% of top ADHD TikToks inaccurate vs ~22% on YouTube. Wide press coverage.",
         "Position as 'lived experience, not medical advice'. Never claim a trait = ADHD. Point people to a doctor. That builds trust.",
         "Evergreen"],
        ["Emotionally expressive, involved dads; unpolished beats produced", "TikTok, IG",
         "2026 creator guidance: younger audiences respond to expressive, involved dads, and everyday raw moments outperform polished ones.",
         "Your raw-and-real rule is already the right call. Film at your gym and in your car, not a studio.", "Evergreen"],
        ["Practical 'dad advice' / how-to format", "TikTok, IG",
         "Dad Advice From Bo: ~4.4M TikTok followers on instructional dad videos.",
         "Every video gives one concrete takeaway (a prompt, a checklist, a script) and puts it on screen so people save it.", "Evergreen"],
        ["Watch time beats length", "TikTok, IG",
         "Hootsuite 2026: watch time and completion rate carry the most weight among engagement signals. One 2026 guide argues "
         "total seconds watched matter, so a 45-second video watched fully beats a 12-second one (a vendor claim; TikTok "
         "hasn't confirmed it).",
         "The rewritten scripts put a new, specific detail every ~10 seconds so 60-75 seconds holds. If week-1 retention "
         "drops before 15 seconds, cut the next video to hook + one detail + CTA (~30 s).",
         "Platform rule"],
        ["Halloween formats (Pumpkin Head Illusion, Ramalama Costume Walk)", "TikTok", "Top October 2026 trends per NewEngen roundup",
         "One light post: 'ADHD dad Halloween prep (it's Oct 30 and I just remembered)'. Use the trending audio quietly under the voiceover.",
         "Ends Oct 31"],
        ["Two Fishes debate format", "TikTok", "October 2026 roundup: used to argue a take, often with parents",
         "Possible stitch-style post: 'Me vs my ADHD brain arguing at 5 AM'. Only if it lands naturally.", "~1-2 weeks"],
        ["Instagram: sends + originality", "IG",
         "Mosseri-attributed signals: watch time, likes per reach, sends per reach. Accounts that mostly repost lose recommendations.",
         "Make videos people DM to their partner ('send this to your wife'). Always upload a clean original, never a TikTok download.",
         "Platform rule"],
        ["TikTok keyword search", "TikTok",
         "TikTok reads captions, on-screen text and speech for keywords. Guides say to put the keyword early.",
         "Say 'ADHD dad' in the first 3 seconds, put it in the first on-screen text, and in the first line of the caption.",
         "Platform rule"],
    ],
)

# ---------------------------------------------------------------------------
# 10. Scripts
# ---------------------------------------------------------------------------
SCRIPT_RULES = [
    "All three are written for the recommended name. If you keep 'Happy', swap 'Healthy' → 'Happy'; nothing else changes.",
    "Story rule: the habit is never named, hinted at, or counted in days. The story is the pattern, the sentence to your "
    "wife, and what came after.",
    "Details: every script ends with a 'Detail check' row. TRUE lines come from what you told me (or your own setup). SWAP "
    "lines are specifics I wrote to make it sound like a real person: keep the ones that are true for you, and replace the "
    "rest with your version.",
    "Length: 60-75 seconds after jump cuts. Captions: word-by-word captions burned in on every line (CapCut auto-captions, "
    "proofread). Big on-screen TEXT sits above the captions.",
    "Audio: talking parts are recorded where there's no gym music (car, entrance, stairwell, quiet corner). Gym-floor shots "
    "are muted B-roll. See Filming Logistics.",
    "Recommended order: B first (Wed), C second (Thu), A third (Fri). Film all three Wednesday morning. Pin all three.",
]

SCRIPTS = (
    "Scripts",
    SCRIPT_RULES,
    ["Script", "Beat", "Time", "On-screen TEXT", "You say (word for word)", "Shot / delivery"],
    [
        # --- Script A: The Parking Lot ---
        ["A: The Parking Lot", "HOOK", "0-4s", "One sentence to my wife. It's why this account exists.",
         "One sentence to my wife. Two months ago. It's the reason this account exists.",
         "Driver's seat, gym lot, engine off, still dark. Phone on the dash at eye level. First word on frame one: no 'hey "
         "guys', no smile yet."],
        ["A: The Parking Lot", "The loop", "4-15s", "Same pattern. Same apology. Same 'this time's different.'",
         "For years I ran the same destructive patterns. Same mistake, same apology, same speech about how this time was "
         "different. I could've given that speech in my sleep. Not a flex.",
         "Dry on 'Not a flex.' Glance away, then back to the lens."],
        ["A: The Parking Lot", "The sentence", "15-26s", "“Something has to change. And I think it's me.”",
         "Then one night I skipped the speech and said, 'Something has to change. And I think it's me.' That was the "
         "turning point. One sentence I'd dodged for years.",
         "Slow down. Hold one full second of silence after 'And I think it's me.'"],
        ["A: The Parking Lot", "The month", "26-40s", "Inside a month: ADHD diagnosis + AI",
         "Inside a month, a doctor said 'ADHD.' About me. It explained a lot. Excused none of it. And I started using AI "
         "for the stuff my brain drops. Last night it checked whether this channel's name was trademarked.",
         "Jump cut between sentences and keep the cuts. Half-smile on 'trademarked.'"],
        ["A: The Parking Lot", "The channel", "40-50s", "AI Dad. Healthy Dad. (Check the first letters.)",
         "So: AI Dad, Healthy Dad. Yes, the first letters spell exactly what you think. I'm two months into learning my own "
         "brain, and I'll show you what's helping, and what isn't.",
         "Small smirk on 'exactly what you think.' Then straight down the lens."],
        ["A: The Parking Lot", "Soft CTA", "50-62s", "Been there? 🚗 below. Got a sentence you haven't said yet? DMs open.",
         "If you've been there, drop a 🚗 in the comments. If you've got your own version of that sentence, the one you "
         "haven't said yet, DM me. I'll read it right here tomorrow, before I go in.",
         "Open the car door on the last word and cut as it opens. That's your ending."],
        ["A: The Parking Lot", "Post copy", "-", "Cover text: 'The sentence that changed everything (ADHD dad)'",
         "CAPTION: Late-diagnosed ADHD dad. Two months ago I told my wife something had to change. Inside a month: the "
         "diagnosis, and AI. This account is what happens next. Lived experience, not medical advice. #adhddad "
         "#latediagnosedadhd #adultadhd #adhd #dadsoftiktok #fatherhood",
         "Pillar: Pattern Breaks"],
        ["A: The Parking Lot", "Detail check", "-", "-",
         "TRUE (from you): the repeating patterns; telling your wife something had to change; that being the turning point; "
         "the diagnosis and AI inside about a month, about two months ago; the gym before the house wakes up. TRUE (from "
         "last night): AI checked whether the channel name was trademarked. SWAP if it isn't yours: 'for years'; the "
         "speech-in-my-sleep line; the exact words of your sentence (use your own; the hook works with any one sentence); "
         "'one night'. ASSUMES you drive to the gym; if not, film on a bench outside the entrance.",
         "Read before filming. Your cue card is the On-screen TEXT column."],
        # --- Script B: The Acronym ---
        ["B: The Acronym (POST FIRST)", "HOOK", "0-3s", "AI Dad Healthy Dad → A.D.H.D.",
         "AI Dad. Healthy Dad. Read the first letters.",
         "Outside the gym doors or in a stairwell, with no speakers in earshot. Point up at the text as it appears. Deadpan."],
        ["B: The Acronym (POST FIRST)", "The payoff", "3-8s", "I didn't notice either. A doctor did.",
         "... Yeah. I didn't notice either. A doctor did. About me. Two months ago.",
         "One beat of silence before 'Yeah.' This line is what makes people stay."],
        ["B: The Acronym (POST FIRST)", "Who", "8-18s", "ADHD dad · late-diagnosed · at the gym before the house wakes up",
         "I'm a dad. It's not even six, I'm at the gym before my house wakes up, and I'm finally learning why my brain does "
         "what it does.",
         "Each fact pops on screen as you say it."],
        ["B: The Acronym (POST FIRST)", "The story", "18-30s", "Same patterns → told my wife → turning point → diagnosis + AI",
         "Short version: same destructive patterns, over and over. Different week, same ending. Then I told my wife something "
         "had to change. That was the turning point. Inside a month: the diagnosis, and AI.",
         "Steady pace. Don't rush 'told my wife.'"],
        ["B: The Acronym (POST FIRST)", "The turn", "30-40s", "AI didn't fix me. It built me a {ROWS}-row spreadsheet.",
         "AI didn't fix me. I asked it to help launch this account, and it built me a {ROWS}-row spreadsheet. I have ADHD. "
         "I've read row one.",
         "Hold up your phone with the sheet open for 2 seconds, then back to camera. Dry: the laugh is theirs, not yours."],
        ["B: The Acronym (POST FIRST)", "Three things (SAVEABLE)", "40-58s",
         "1. The gym before the house wakes up\n2. AI as my external brain (real prompts)\n3. Dad life with a brain that finally has a name",
         "So I asked for the short version. One: the gym before my house wakes up, the only quiet hour I get. Two: AI as my "
         "external brain, real prompts, real screens. Three: dad life with a brain that finally has a name. Including the "
         "parts I'm still bad at.",
         "Fingers up for 1-2-3; each item stacks on screen so people screenshot it. One second of muted B-roll per item: "
         "the gym clock, your phone screen, your gym bag."],
        ["B: The Acronym (POST FIRST)", "Soft CTA", "58-67s", "Just diagnosed? Wondering? Say hi 👇",
         "Dads: just got the diagnosis? Or watching this going 'hang on...'? Say hi in the comments. You don't need it "
         "figured out. I clearly don't.",
         "Small smile on 'I clearly don't.' End on the last word."],
        ["B: The Acronym (POST FIRST)", "Post copy", "-", "Cover text: 'AI Dad Healthy Dad = ADHD'",
         "CAPTION: ADHD dad here. Late-diagnosed two months ago. At the gym before the house wakes up, using AI as my "
         "external brain, figuring the rest out on camera. Lived experience, not medical advice. #adhddad "
         "#latediagnosedadhd #adultadhd #adhdtiktok #dadsoftiktok #5amclub #ai",
         "Pillar: Intro / all"],
        ["B: The Acronym (POST FIRST)", "Detail check", "-", "-",
         "TRUE (from you): the acronym; diagnosed about two months ago; patterns → told your wife → turning point → "
         "diagnosis and AI inside about a month; the gym before the house wakes up. TRUE (from tonight): AI built you this "
         "launch spreadsheet, which has {ROWS} rows as of Oct 13 (if you add rows, update the number or say 'a giant "
         "spreadsheet'). SWAP if it isn't yours: 'It's not even six' (say your real time); 'the only quiet hour I get'; the "
         "B-roll items (use what's actually there).",
         "Read before filming. Your cue card is the On-screen TEXT column."],
        # --- Script C: 5:40 AM ---
        ["C: 5:40 AM", "HOOK", "0-4s", "5:40 AM. The only hour my ADHD brain shuts up.",
         "5:40 a.m. The only hour my ADHD brain isn't running fourteen tabs.",
         "Between sets; a little out of breath is fine. Quietest corner, back to a wall, no mirrors. If gym music is audible "
         "on playback, re-record your lines in the car and use these shots as muted B-roll."],
        ["C: 5:40 AM", "Who", "4-15s", "ADHD dad · told my wife something had to change · diagnosis + AI inside a month",
         "Quick version: I'm a dad. Years of the same destructive patterns. Two months ago I told my wife something had to "
         "change. Inside a month: an ADHD diagnosis, and AI.",
         "Sit on the bench. Wipe your face mid-sentence: it reads as real, and it's a natural jump-cut point."],
        ["C: 5:40 AM", "The insight", "15-27s", "It's not about doing MORE. Nobody needs anything from me yet.",
         "This hour isn't about getting more done. It's that nobody needs anything from me yet. No questions. No "
         "notifications. No 'Dad, where's my...' One bar, one decision. Closest my brain gets to quiet.",
         "Cut to muted B-roll on 'One bar': hands on the barbell, the plates, the empty floor."],
        ["C: 5:40 AM", "The reset", "27-32s", "My checklist resets at 3 AM. Yesterday doesn't get a vote.",
         "My checklist resets itself at 3 a.m. Yesterday doesn't get a vote.",
         "Optional 2-second shot of the checklist on your phone screen."],
        ["C: 5:40 AM", "The 3 calls (SAVEABLE)", "32-52s",
         "Between sets, 3 calls:\n1. The ONE thing that has to happen today\n2. When the old pattern's most likely to show up today (and what I'll do instead)\n3. One thing with my kids. Phone in a drawer.",
         "Between sets I make three calls before the day makes them for me. One: the one thing that has to happen today. "
         "One, not five. Two: when the old pattern's most likely to show up, and what I'll do instead. Three: one thing with "
         "my kids, phone in a drawer. Then AI nags me till bedtime.",
         "Count on your fingers. Each item stacks on screen: this is the part people save."],
        ["C: 5:40 AM", "Channel + soft CTA", "52-63s", "AI Dad. Healthy Dad. What time did you get up?",
         "This is AI Dad, Healthy Dad. The initials are on purpose. Up this early too? Drop the time you got up. If not, DM "
         "me what your mornings look like now. Rough is fine.",
         "Stand up, last line to camera, walk back to the bar. Cut."],
        ["C: 5:40 AM", "Post copy", "-", "Cover text: 'The 3 calls I make at 5:40 AM (ADHD dad)'",
         "CAPTION: ADHD dad morning routine, but not for productivity. It's for getting ahead of my brain before the day "
         "starts. The 3 calls are on screen; save it for tomorrow. Lived experience, not medical advice. #adhddad #adhd "
         "#morningroutine #5amclub #adultadhd #dadsoftiktok #gymtok",
         "Pillar: 5AM Brain"],
        ["C: 5:40 AM", "Detail check", "-", "-",
         "TRUE (from you): morning person; gym in the morning; patterns → told your wife → diagnosis and AI inside about a "
         "month. CHECK (from your own Make account, seen while I checked its Google access): an automation named 'Checklist – "
         "Daily 3am Refresh'. Keep the 3 a.m. line only if that really resets your checklist; cut it if you'd rather not "
         "share it. SWAP if it isn't yours: '5:40' (your real time; change the hook text and cover too); 'Dad, where's my...' "
         "(use what your kids actually ask); 'years' of patterns.",
         "Read before filming. Your cue card is the On-screen TEXT column."],
    ],
)

# ---------------------------------------------------------------------------
# 11. Bio
# ---------------------------------------------------------------------------
BIO = (
    "Bio",
    ["Sharpened with the trend terms already in this sheet: 'late-diagnosed', 'ADHD dad', '5AM', 'external brain', and "
     "'lived experience, not medical advice' (the misinformation-backlash trend). Name fields are what both apps search "
     "hardest. Character counts are checked against platform limits."],
    ["Platform", "Field", "Copy (paste exactly)", "Chars / limit", "Notes"],
    [
        ["TikTok", "Name", "ADHD Dad | AI Dad Healthy Dad", "29 of 30", "Searchable. 'ADHD Dad' first so it shows in search previews."],
        ["TikTok", "Username", "@aidadhealthydad", "16 of 24", ""],
        ["TikTok", "Bio", "Late-diagnosed ADHD dad · 5AM gym\nAI = my external brain · DMs open", "{TT_BIO_LEN} of 80",
         "Each term comes from this sheet's trend list (late-diagnosed, ADHD dad, 5AM, external brain). Soft CTA = 'DMs open'."],
        ["Instagram", "Name", "AI Dad Healthy Dad | Late-Diagnosed ADHD Dad", "{IG_NAME_LEN} of 64",
         "Instagram searches the name field hardest, so it carries the top trend term. Instagram limits name changes (twice "
         "in 14 days), so set it once."],
        ["Instagram", "Username", "@aidadhealthydad", "16 of 30", ""],
        ["Instagram", "Bio",
         "Late-diagnosed ADHD dad\n5AM gym before the house wakes up\nAI = my external brain, real prompts\nReal dad, no AI faces · not medical advice\nDMs open",
         "{IG_BIO_LEN} of 150",
         "Lines 1-3 are search terms. Line 4 is the trust signal: the misinformation-backlash trend, and 'AI Dad' shouldn't "
         "read as an AI persona. Category: Digital creator. Add the link once aidadhealthydad.com is live."],
        ["Both", "Pinned / Highlights", "Pin Scripts B, C, A on TikTok. Instagram Highlights: 'Start Here', '5AM Gym', 'AI Prompts', 'Diagnosis Log'.", "-", ""],
    ],
)

# ---------------------------------------------------------------------------
# 12. Content Pillars
# ---------------------------------------------------------------------------
PILLAR_1_IDEAS = [
    "The only hour nobody needs anything from me: why 5 AM is regulation, not productivity. Save: the 3 calls.",
    "Notifications off until my last set (yes, I film on this phone): what my brain does when I check them first. Save: the notifications-last rule.",
    "Yesterday doesn't get a vote: the checklist that resets at 3 AM, and why a fresh start every morning matters with ADHD. Save: a reset checklist.",
    "If the gym bag isn't packed by 9 PM, I don't go: killing morning decisions the night before. Save: the 4-item night-before list.",
    "One bar, one decision: why lifting is the only time my brain single-tasks. Save: how to get one single-task block at home.",
    "The morning after a bad day: what I do differently when yesterday went sideways. Save: the 3-step restart.",
    "5 AM me vs 9 PM me: same guy, different brain, and the note morning me leaves for bedtime me. Save: the hand-off note.",
    "What I do in the 90 seconds between sets: one voice memo to AI. Save: the exact voice-memo prompt.",
    "When the alarm doesn't work: the 10-minute version of my morning. Save: the minimum viable morning.",
    "I don't set goals at 5 AM, I set defaults: breakfast, first task, phone. Save: my 3 defaults.",
    "The drive home is my planning meeting: by the time I park, I know the first three things I'm doing inside. Save: the 3 questions I ask on the drive.",
    "What lifting taught me about ADHD that the diagnosis didn't: add 5 lb, not 50. Save: the 5-lb rule for habits.",
    "Sunday 6 AM: the whole week in 15 minutes, with AI. Save: the Sunday prompt.",
    "Can't do 5 AM? It's the quiet, not the clock: how to find your quiet hour. Save: a 3-day test to find yours.",
    "The ADHD guy who's a morning person: why it works for me (lived experience, not advice). Save: a test-it-yourself checklist.",
]

PILLAR_2_IDEAS = [
    "The prompt I use when I can't start anything: 'give me a 2-minute first step'. Save: the prompt.",
    "Brain dump → 3 things in 30 seconds: voice memo in, top 3 out. Save: the prompt.",
    "The school flyer trick: photo of the flyer, AI turns it into reminders. Save: the 3-step workflow.",
    "The worry sort: voice-memo everything on my mind, and AI sorts it into today / this week / not mine. Save: the sorting prompt.",
    "I asked AI if my channel name was trademarked: what it found, and what it said I still had to check myself. Save: the 'verify it yourself' list.",
    "AI built me a {ROWS}-row spreadsheet. Here's how I made it useful: 'just tell me this week's 3 things'. Save: the shrink-it prompt.",
    "The 'am I sliding?' check-in: one sentence to AI when the old pattern starts, and it asks me 3 questions back. Save: the 3 questions.",
    "'Remind me later' → a real calendar event in 10 seconds, hands-free. Save: the dictation phrasing that works.",
    "What I will NOT use AI for: talking to my kids, apologizing to my wife, health decisions. Save: my human-only list.",
    "AI as a body double: 'check on me every 10 minutes while I do the dishes'. Save: the prompt.",
    "The email I've been avoiding: AI writes the first sentence, I write the rest. Save: the prompt.",
    "Planning a kid's birthday backward from the date. Save: the backward-plan prompt.",
    "My lifting log builds itself every Saturday: the one boring thing I automated first (check: from your Make automation name). Save: how to pick your first automation.",
    "Prompts that made it worse: the 40-item list, the generic pep talk. Save: how to ask for less.",
    "Getting ready for a doctor's appointment: AI organizes my notes and questions; the doctor gives the answers. Save: the appointment-prep prompt.",
]

PILLAR_3_IDEAS = [
    "The week after the diagnosis: relief, then a weird kind of grief, then 'now what?' Save: what actually helped that week.",
    "Explained, not excused: the rule I set the day I found out. Save: the rule, in one line.",
    "What I thought ADHD looked like vs what it looks like on me. Save: my 5 surprises (not a checklist for diagnosing anyone).",
    "The questions I took to my appointment. Save: the list (bring your own to a doctor).",
    "Re-reading my own history: the moments that make more sense now. Save: how to look back without spiraling.",
    "Things I wanted to blame on ADHD that weren't ADHD. Save: the 'ask a professional' list.",
    "How I filter ADHD content online now (a 2026 study rated ~52% of top ADHD TikToks inaccurate). Save: my 3-question filter.",
    "Month-2 check-in: what's working, what isn't (repeat monthly). Save: the one-page scorecard.",
    "Deciding who to tell, and who doesn't need to know yet. Save: the who/when/how list.",
    "ADHD at work: the one change that made the biggest difference. Save: the change.",
    "The diagnosis didn't fix the patterns. Here's what it did do. Save: 3 things a name gives you.",
    "What my wife noticed before I did (only with her OK). Save: 3 questions to ask your partner.",
    "How we talk about brains at home with the kids: no labels, no lectures. Save: kid-friendly phrases.",
    "Late-diagnosed dads: what I wish someone had told me at 20. Save: the list.",
    "The 3 tools I'd keep if I could only keep 3. Save: the 3.",
]

PILLAR_4_IDEAS = [
    "The sentence that changed everything, and how to say yours. Save: 3 ways to start the conversation.",
    "The 3 signs my loop is starting: going quiet, skipping the gym, 'I'll deal with it tomorrow'. Save: build your own early-warning list.",
    "Apologies with an action attached. Save: the formula (what I did / what it cost you / what I'm doing differently by [date]).",
    "Why 'this time's different' never worked: promises vs systems. Save: turn one promise into one system.",
    "The first 10 minutes when the old pattern shows up. Save: my 10-minute plan.",
    "Telling your partner: what I'd do differently. Save: the do/don't list.",
    "'I'll remember': why my wife stopped accepting it, and what replaced it. Save: the shared-list setup.",
    "Shame is not a strategy: why beating myself up kept the loop running. Save: the shame → next step swap.",
    "Patterns live in calendars: how to map when and where yours shows up (I share the method, not my map). Save: the 7-day pattern map.",
    "The friend I told second: accountability without a speech. Save: what to ask a friend for.",
    "Repair with your kids: saying sorry so a kid actually gets it. Save: the kid-sized repair script.",
    "What week 3 of breaking a pattern actually felt like. Save: what to expect.",
    "Replace, don't just remove: what I put in the gap. Save: the replacement list.",
    "The setback video: when the old pattern wins a round, what I do next (film it only when it's real). Save: the setback plan.",
    "Two months in: what's actually different at home. Save: 3 signs of progress that aren't perfection.",
]

PILLAR_5_IDEAS = [
    "Things I lost this week, ranked. Fix: one landing spot by the door.",
    "Parent-teacher night with ADHD. Fix: 3 questions in my notes app before I walk in.",
    "Six cold coffees around the house: an ADHD dad mystery. Fix: one mug, one spot.",
    "Bedtime routine, ADHD dad edition. Fix: a picture checklist (for the kids and for me).",
    "Halloween prep, Oct 30 (seasonal; post by Oct 31). Fix: plan backward from the date.",
    "I walked into the gym and forgot what day it was. Fix: the week's plan on my lock screen.",
    "Grocery store with ADHD: a nature documentary. Fix: a list sorted by aisle (AI does it).",
    "Fourteen tabs open at bedtime. Fix: tab dump to AI, then close everything.",
    "School pickup: the 2:58 panic. Fix: a labeled alarm, not just a time.",
    "Building kids' furniture with ADHD. Fix: AI reads me the next step only.",
    "Explaining my new 'system' to my family for the fourth time. Fix: keep systems boring.",
    "Hyperfocus: I went to the garage to fix one thing. Fix: a timer before I start.",
    "Things my kids have already figured out about my brain (with their OK). Fix: the one thing I changed because of them.",
    "ADHD dad 'multitasking', honestly. Fix: one thing at a time, said out loud.",
    "Packing school lunches at 6:45 AM with ADHD. Fix: the same five lunches on rotation.",
]


def numbered(ideas):
    return "\n".join(f"{i}) {idea}" for i, idea in enumerate(ideas, 1))


PILLARS = (
    "Content Pillars",
    ["Weekly rhythm: Mon AI External Brain · Tue Pattern Breaks · Wed 5AM Brain · Thu ADHD Dad in the Wild · Fri Late-Diagnosis Log · "
     "Sat reply-to-comment video + IG carousel · Sun batch-film. 5 pillars × 15 ideas = 75 videos, about 15 weeks at 5 a week. "
     "Every video carries one saveable thing (prompt, checklist, or script)."],
    ["Pillar", "What it is", "Saveable element", "Ready-to-film ideas (15)", "Format"],
    [
        ["1. 5AM Brain",
         "Early mornings at the gym, before the house wakes up, as ADHD regulation, not hustle: quiet before demand, and "
         "decisions made before the day makes them for you.",
         "Morning checklists and the '3 calls' card",
         numbered(PILLAR_1_IDEAS),
         "Filmed at the gym (talking parts in a music-free spot) or in the car after. Weekly IG carousel."],
        ["2. AI External Brain",
         "Exactly how you use AI for the ADHD gaps: starting, remembering, planning, follow-through. Real screens and real "
         "prompts, failures included.",
         "Copy-paste prompts in the caption",
         numbered(PILLAR_2_IDEAS),
         "Talking head + 3-5 s screen recording. Show the prompt, then the result. Never show private info on screen."],
        ["3. Late-Diagnosis Log (new; replaces the old pillar 3)",
         "Two months in and counting: what the ADHD diagnosis changed, what it didn't, and what you're still figuring out. "
         "Honest updates from a late-diagnosed dad. Lived experience, not medical advice.",
         "Question lists and 'what helped' lists",
         numbered(PILLAR_3_IDEAS),
         "Weekly on Fridays. Same opener every time: 'Late-diagnosed, week [X].' Car or quiet corner."],
        ["4. Pattern Breaks",
         "The loop, the sentence to your wife, and the repair. Practical and specific. The pattern itself is never named, "
         "and the tools work for any pattern.",
         "Scripts, sentences and formulas",
         numbered(PILLAR_4_IDEAS),
         "Talking head, slower pace, car or quiet corner. Strong 'send this to your partner' potential (Instagram sends)."],
        ["5. ADHD Dad in the Wild",
         "Dry-humor everyday moments: lost keys, school forms, fourteen tabs at bedtime. Each one ends with one actual fix.",
         "The one fix at the end",
         numbered(PILLAR_5_IDEAS),
         "POV / skit-lite / voiceover over B-roll. The easiest on-ramp for new viewers."],
        ["Recurring format: Comment Answers",
         "Reply to the best comment or DM question with a video, so the audience fills your calendar for you.",
         "The answer itself",
         "Use TikTok's 'reply with video' on the top question each week. Turn DM themes into posts (anonymized).",
         "Saturdays. Keeps you from running dry by week 2."],
    ],
)

# ---------------------------------------------------------------------------
# 13. Assumptions (+ re-check log)
# ---------------------------------------------------------------------------
# Filled in after each review pass: what the pass caught and how it was fixed.
RECHECK_LOG = [
    ["22", "RE-CHECK 1 (automated: hint words, character limits, idea counts, script timing, placeholders, cross-references) "
           "caught: all three scripts ran long, about 87, 87 and 100 seconds at a natural speaking pace against the 60-75 s "
           "target, and their timestamps didn't match their word counts.",
     "Fixed: cut each to 170-180 spoken words (now about 67-73 s) without dropping a specific detail, and re-timed every beat."],
    ["23", "RE-CHECK 1 caught: the Instagram bio was 153 characters (limit 150).",
     "Fixed: trimmed to 146 by dropping the emoji and two words."],
    ["24", "RE-CHECK 1 caught: hint words that survived in public copy: 'every morning starts clean' (Script C), 'when I slip' "
           "(a Pattern Breaks idea), '5 AM me vs 5 PM me' (an echo of the old story), plus 'Day 1' labels that read like a "
           "day count.",
     "Fixed: replaced each ('Yesterday doesn't get a vote', 'when the old pattern wins a round', '9 PM', 'First post'). The "
     "checker now blocks these words in scripts, bios, pillars and the calendar."],
    ["25", "RE-CHECK 2 (reading for depth and specificity) caught: Scripts A and B used the same '...Yeah' acronym reveal, "
           "which would read as a template across one week, and Script C's 'Say it fast, you'll get it' was simply wrong "
           "(saying the name fast doesn't spell ADHD).",
     "Fixed: A now says 'Yes, the first letters spell exactly what you think'; C says 'The initials are on purpose.'"],
    ["26", "RE-CHECK 2 caught: Script A's CTA told viewers not to comment, which throws away an easy engagement signal.",
     "Fixed: it now invites a 🚗 comment from anyone who's been there and keeps the DM for the personal part."],
    ["27", "RE-CHECK 2 caught: 7 of the 75 pillar ideas overlapped, contradicted something, or risked too much: 'I'll "
           "remember' covered in two pillars (plus a third angle), the gym bag twice, the 3 AM checklist twice, 'my phone "
           "stays in the car' contradicting filming on your phone, a drive-home idea that mixed up the gym lot and your "
           "front door, and a Pattern Breaks idea (mapping when your pattern shows up) that could reveal the habit's timing "
           "on camera.",
     "Fixed: replaced with distinct ideas (notifications-off, the worry sort, six cold coffees, school lunches) or "
     "reworded ('remind me later', 'I share the method, not my map')."],
    ["28", "RE-CHECK 2 caught three accuracy slips in Filming Logistics: 'after the mic, the cheapest upgrade' was backwards "
           "(the tripod costs less than the mic), the Instagram help-center claim was broader than the source, and I'd "
           "called CapCut's 'Reduce noise' free without checking.",
     "Fixed: reworded all three to match the sources, and named the most-cited tripod (EUCOS 62-in, with the TONEOF 68-in "
     "as the sturdier option)."],
    ["29", "RE-CHECK 3 (consistency across sections) caught: the week-1 calendar put the reply-to-comment video on Tuesday, "
           "while the weekly rhythm says Saturday (Tuesday is Pattern Breaks).",
     "Fixed: moved it to Sat Oct 17 at 7:00 AM, put a Pattern Breaks idea on Tue Oct 20, and noted that launch week runs "
     "the three intro scripts first."],
    ["30", "RE-CHECK 3 caught: three places told you to use each script's Detail check row as your bullet card, but those "
           "rows are truth checklists, not delivery cues.",
     "Fixed: your cue card is each script's On-screen TEXT column; the Detail check rows are for reading the night before."],
    ["31", "RE-CHECK 3 also re-tested the name recommendation against the corrected story, and matched every script name, "
           "pillar name, price and time across sections.",
     "No change needed: the name call rests on trademark and search crowding, which didn't change, and the names, prices "
     "and times now match everywhere."],
]

ASSUMPTIONS = (
    "Assumptions",
    ["Every assumption I made instead of asking you, then the re-check log: what I caught and fixed on each review pass "
     "before marking the work done."],
    ["#", "Assumption", "Why / impact if wrong"],
    [
        ["1", "You're US-based and posting to a US English-speaking audience; times are US Eastern (America/New_York).", "If you're in another time zone, shift the clock times. The logic (morning, TikTok first) holds."],
        ["2", "First post: 7:30 AM ET on Wed Oct 14 (moved from 7:00 so you can film at the gym and still have 45 minutes to edit); 7:00 AM ET from Thursday.", "If you film the night before instead, go back to 7:00."],
        ["3", "Corrected story, used everywhere: the same destructive patterns, over and over → you finally admitted to your wife that something needed to change (the turning point) → ADHD diagnosis and AI inside about a month, about two months ago. The habit is never named or hinted at, and nothing counts days.", "If the order differs (for example, AI came before the diagnosis), swap the two in the scripts; nothing else depends on it."],
        ["4", "The old third pillar was replaced by 'Late-Diagnosis Log' to keep five pillars after the story correction.", "It uses the sheet's strongest trend (late-diagnosed ADHD dads). Swap it out if you'd rather have a different fifth topic."],
        ["5", "You have more than one child ('the kids'). No names, ages or genders are used.", "Change to 'my kid' if you have one. Keep the kids anonymous on camera until you decide your privacy rules."],
        ["6", "Your own name isn't used in the scripts or bios.", "Add 'I'm [name]' after the hook if you want a personal brand; it isn't needed for search."],
        ["7", "Script details are labeled TRUE (from you, or from tonight's work) or SWAP (specifics I wrote to make it sound like a real person). Two details come from your own Make automations, which I saw while checking Make's Google access: a daily 3 AM checklist refresh and a weekly lifting tab. Keep them only if they're accurate and you're happy sharing them.", "Never say a SWAP line on camera unless it's true for you. Each script's Detail check row lists them."],
        ["8", "You drive to the gym, so Script A is filmed in the car in the gym lot.", "If you don't drive, film A on a bench outside the entrance; the words still work."],
        ["9", "Trademark 'clearance search' = searching USPTO data through indexed mirrors (Justia, Trademarkia, uspto.report, TTABVUE), because this sandbox blocks tmsearch.uspto.gov directly.", "Run the 5 listed queries yourself, and get an attorney's opinion before filing. This is not legal advice."],
        ["10", "Handles and domains are 'no existing use found', not 'confirmed available', because live lookups were blocked.", "Claim them tonight to settle it. Fallbacks are listed in the Handles & Domains section."],
        ["11", "Because 'Healthy' had no real problem, alternatives weren't strictly required; I checked three backups anyway.", "AI Dad Hopeful Dad is the cleanest backup."],
        ["12", "You'll eventually sell coaching (USPTO Class 41) and maybe merch (Class 25); the trademark risk is judged against those.", "If you never sell merch, Happy Dad's risk drops somewhat. The search and brand-confusion problems remain."],
        ["13", "Your connected Metricool brand (ID 6987872) is the one for this project. It currently has no social networks connected, so I couldn't pull personalized best times or schedule posts.", "Once TikTok and Instagram are connected, I can pull Best Times and schedule posts for you."],
        ["14", "TikTok starts as a personal/creator account, not Business, to keep access to commercial trending sounds.", "Switch to Business later if you need custom thumbnails through Metricool or business tools."],
        ["15", "Purchases: a tripod with remote ($20-40), a noise-cancelling clip mic (~$79 on sale), and the domain (~$10-20/yr). Optional: a magnetic gym mount ($25-60) and PromptSmart (~$9.99/mo).", "Prices come from 2026 reviews and listings and move often; check before buying."],
        ["16", "Content is lived experience, not medical advice; the scripts make no medical claims about ADHD.", "Protects trust in a niche known for misinformation (the ~52% figure)."],
        ["17", "Trend data is as of Oct 13, 2026; trend-specific items expire within 1-2 weeks.", "Recheck TikTok Creative Center weekly (Monday, 10 min)."],
        ["18", "Per your instruction, scripts, pillars and bios use only research already in this sheet. Filming Logistics is new research, because you asked for it.", "-"],
        ["19", "Guardrails followed: no emails sent, nothing pushed to GitHub, nothing deleted. Repo changes are committed locally only.", "Push when you're ready."],
        ["20", "This sheet was updated in place (same file, same link). There's no Google Sheets connector in this session, so I wrote it through your Make account's existing Google connection with a one-off scenario: 'AI Dad: launch sheet writer (Claude, one-off)'. I switched it off after the run and left it in your Make account, because of the no-deletions rule.", "Delete that scenario in Make whenever you like; it doesn't run on its own. Drive's version history has tonight's earlier version if you ever want it back. "
         "RE-CHECK 4 (after writing): I downloaded this sheet and compared all 296 rows to the source. Sheets had auto-converted 20 "
         "cells ('$0' became 0, and the calendar dates became date numbers), so I rewrote those as text and re-checked: 0 differences."],
        ["21", "Third-party claims (Metricool free-tier limits, USPTO fee, study figures, gym-chain policies, Instagram reach effects) are as reported by their sources and flagged where I couldn't confirm them first-hand. Product hold-strength claims are vendor marketing.", "Check pricing and policy pages before relying on them."],
    ] + RECHECK_LOG,
)

# ---------------------------------------------------------------------------
# 14. Sources
# ---------------------------------------------------------------------------
SOURCES = (
    "Sources",
    ["Gathered via web search on " + RESEARCH_DATE + " (filming sources added the night of Oct 13). Direct page fetches were blocked by the sandbox network policy."],
    ["Topic", "Source", "URL"],
    [
        ["Trademark", "HAPPY DAD SN 90229564 (Justia)", "https://trademarks.justia.com/902/29/happy-90229564.html"],
        ["Trademark", "HAPPY DAD HARD SELTZER SN 90573863 (Justia)", "https://trademarks.justia.com/905/73/happy-dad-hard-90573863.html"],
        ["Trademark", "HAPPY DAD HARD SELTZER SN 90573863 (Trademarkia)", "https://www.trademarkia.com/happy-dad-hard-seltzer-90573863"],
        ["Trademark", "HAPPY DAD HARD SELTZER SN 90980249 (Justia)", "https://trademarks.justia.com/909/80/happy-dad-hard-90980249.html"],
        ["Trademark", "HAPPY DAD HARD SELTZER MOM SN 98248506 (Justia)", "https://trademarks.justia.com/982/48/happy-mom-hard-98248506.html"],
        ["Trademark", "Happy Dad, LLC owner page (Justia)", "https://trademarks.justia.com/owners/happy-dad-llc-4737642"],
        ["Trademark", "Happy Dad, LLC portfolio (uspto.report)", "https://uspto.report/company/Happy-Dad-L-L-C"],
        ["Trademark", "TTAB Opposition 91295385", "https://ttabvue.uspto.gov/ttabvue/v?pno=91295385&pty=OPP"],
        ["Trademark", "COACH DAD SN 98172423", "https://trademark.justia.com/981/72/coach-98172423.html"],
        ["Trademark", "POSITIVELY DAD SN 90007646", "https://trademark.justia.com/900/07/positively-90007646.html"],
        ["Trademark", "THE DAD'S GROUP CHAT PODCAST SN 90031850", "https://trademarks.justia.com/900/31/the-dad-s-group-chat-90031850.html"],
        ["Trademark", "THE HOPEFUL MAMA SN 98500313", "https://trademarks.justia.com/985/00/the-hopeful-98500313.html"],
        ["Trademark", "USPTO trademark search", "https://www.uspto.gov/trademarks/search"],
        ["Brand", "Nelk launches Happy Dad (Tubefilter)", "https://www.tubefilter.com/2021/06/01/nelk-launches-happy-dad-hard-seltzer-brand/"],
        ["Brand", "Happy Dad expansion (Brewbound)", "https://www.brewbound.com/news/happy-dad-expands-into-missouri-and-wisconsin-with-breakthru-beverage-group"],
        ["Healthy Dad uses", "The Healthy Dad blog", "https://thehealthydad.com/"],
        ["Healthy Dad uses", "Healthy Dad Convos podcast", "https://podcasts.apple.com/us/podcast/healthy-dad-convos/id1735631538"],
        ["Healthy Dad uses", "Healthy Dads, Healthy Kids (Univ. of Newcastle)", "https://www.newcastle.edu.au/research/research-impact/healthy-dads-healthy-kids"],
        ["Alternatives", "Human Dad apparel brand", "https://humandad.com/"],
        ["Alternatives", "Human Dad Instagram", "https://www.instagram.com/humandadbrand/"],
        ["Alternatives", "The Honest Dad (Instagram)", "https://www.instagram.com/thehonestdad/"],
        ["Alternatives", "The Honest Dad Co. Podcast", "https://podcasts.apple.com/us/podcast/the-honest-dad-co-podcast/id1655527483"],
        ["Timing", "Buffer: best time to post on TikTok 2026", "https://buffer.com/resources/best-time-to-post-on-tiktok/"],
        ["Timing", "Metricool: best time to post on TikTok 2026", "https://metricool.com/best-time-post-tiktok/"],
        ["Timing", "Breakreach: 5 TikTok studies compared", "https://www.breakreach.com/guides/best-time-to-post-on-tiktok"],
        ["Timing", "SocialPilot: best time to post Reels 2026", "https://www.socialpilot.co/insights/best-time-to-post-reels-on-instagram"],
        ["Timing", "Buffer: best time to post on Instagram (Sep 2026)", "https://buffer.com/resources/when-is-the-best-time-to-post-on-instagram/"],
        ["Timing", "Hopper HQ: Instagram 2026", "https://www.hopperhq.com/blog/best-time-to-post-on-instagram/"],
        ["Tools", "Metricool: schedule TikTok posts", "https://metricool.com/schedule-tiktok-videos/"],
        ["Tools", "Metricool: best time to post (Best Times feature)", "https://metricool.com/best-time-to-post-social-networks/"],
        ["Tools", "Edits vs CapCut vs Captions (Creatorflow)", "https://creatorflow.so/blog/best-video-editing-app-instagram-reels/"],
        ["Tools", "Captions vs CapCut (Storycut)", "https://www.storycut.com/compare/captions-vs-capcut"],
        ["Tools", "Teleprompter apps (Jupitrr, Aug 2026)", "https://jupitrr.com/best/teleprompter-apps-for-content-creators"],
        ["Algorithm", "Hootsuite: TikTok algorithm 2026", "https://blog.hootsuite.com/tiktok-algorithm/"],
        ["Algorithm", "Buffer: TikTok algorithm 2026", "https://buffer.com/resources/tiktok-algorithm/"],
        ["Algorithm", "Metricool: TikTok SEO 2026", "https://metricool.com/tiktok-seo/"],
        ["Algorithm", "Buffer: Instagram algorithm 2026", "https://buffer.com/resources/instagram-algorithms/"],
        ["Algorithm", "Instagram originality (Exemplary)", "https://exemplary.ai/blog/instagram-algorithm-original-content"],
        ["Trends", "October 2026 TikTok trends (NewEngen)", "https://newengen.com/insights/october-tiktok-trends/"],
        ["Trends", "TikTok search: dad undiagnosed adhd", "https://www.tiktok.com/discover/dad-undiagnosed-adhd"],
        ["Trends", "ADHD misinformation on TikTok (Euronews, Mar 2026)", "https://www.euronews.com/2026/03/20/tiktok-leads-social-media-platforms-in-mental-health-misinformation-study-finds"],
        ["Trends", "Dad Advice From Bo (Wikipedia)", "https://en.wikipedia.org/wiki/Dad_Advice_From_Bo"],
        ["Trends", "Father's Day creative tips 2026 (Ecomdy)", "https://ecomdymedia.com/blog/father-day-creative-tips"],
        ["Filming", "Metric Coach: best gym tripod under $25", "https://metric.coach/articles/best-gym-tripod-for-phones"],
        ["Filming", "Muscle Madness HQ: best gym tripods 2026", "https://musclemadnesshq.com/best-gym-tripods/"],
        ["Filming", "Kingsway Gym: gym tripod buying guide", "https://kingswaygym.com/gym-tripod/"],
        ["Filming", "Lisa Johnson Fitness: best tripods for gym 2026", "https://www.lisajohnsonfitness.com/best-tripods-for-gym/"],
        ["Filming", "Blaubeck: magnetic gym phone mount (vendor)", "https://blaubeck.com/blogs/product-use/finally-a-gym-phone-mount-that-won-t-let-you-down"],
        ["Filming", "SmallRig 5460 MagSafe gym mount (Adorama listing)", "https://www.adorama.com/smallrig-5460-magsafe-magnetic-phone-mount-gym-recording/p/sr5460"],
        ["Filming", "MagSafe gym magnet mount (Amazon listing; steel only)", "https://www.amazon.com/MagSafe-Magnet-Mount-Squat-Holder/dp/B0GGYZCCP8"],
        ["Filming", "DJI Mic Mini review (New Atlas)", "https://newatlas.com/electronics/dji-mic-mini-review/"],
        ["Filming", "DJI Mic Mini 2S review (TechRadar)", "https://www.techradar.com/cameras/camera-accessories/dji-mic-mini-2s-review"],
        ["Filming", "DJI Mic Mini price drop (Kotaku)", "https://kotaku.com/dji-liquidates-its-mic-mini-at-a-record-low-noise-cancelling-and-hq-audio-now-cost-peanuts-2000639685"],
        ["Filming", "TikTok Creator Academy: muted videos and the music copyright check", "https://www.tiktok.com/creator-academy/article/appeal-muted-video"],
        ["Filming", "TikTok Discover: audio muted by music near the mic (creator-reported)", "https://www.tiktok.com/discover/why-is-my-sound-muted-due-to-copyright-restrictions"],
        ["Filming", "Instagram Help: what audio you can use in reels", "https://help.instagram.com/329208821595430"],
        ["Filming", "Audio unavailable on Reels: fixes (InspireToThrive, 2026)", "https://inspiretothrive.com/audio-unavailable-on-instagram-reels/"],
        ["Filming", "Instagram Reels music copyright rules 2026 (LastPlayDistro)", "https://lastplaydistro.com/blog/instagram-reels-music-copyright-rules-2026-what-artists-creators-must-know"],
        ["Filming", "Copyrighted music on Instagram, business accounts (Fox Music)", "https://www.foximusic.com/blog/instagram-reels-music-copyright-legal-guide/"],
        ["Filming", "Remove background noise in CapCut (guide, Aug 2026)", "https://capcutguide.com/remove-background-noise-capcut/"],
        ["Filming", "CapCut vocal isolation on mobile (creator tutorial)", "https://www.tiktok.com/@adrianvideoimage/video/7468217875396840722"],
        ["Filming", "Edits app listing: audio enhancement (App Store)", "https://apps.apple.com/us/app/edits-video-editor/id6738967378"],
        ["Filming", "Creator report: Edits enhancement glitches at cuts (Threads)", "https://www.threads.com/@priyamdatta/post/DNxOM-M3h0Q/the-edits-app-by-instagram-has-some-flaws-that-need-to-be-sorted-soon-for-it-to-"],
        ["Filming", "Gyms to influencers: stop filming (Axios, 2025)", "https://www.axios.com/2025/05/03/gym-influencer-film-workout-tiktok"],
        ["Filming", "Everyone's talking about filming in gyms (Health Club Management)", "https://www.healthclubmanagement.co.uk/health-club-management-features/Everyones-talking-about-filming-in-gyms/38500"],
        ["Filming", "PureGym filming rule (STV News)", "https://news.stv.tv/world/gym-fluencers-urged-to-stop-filming-in-public-amid-privacy-concerns"],
    ],
)

TABS = [START_HERE, NAME_DECISION, TRADEMARK, HANDLES, ALTERNATIVES, TOOLS, FILMING, TIMING, WEEK1, TRENDS,
        SCRIPTS, BIO, PILLARS, ASSUMPTIONS, SOURCES]
