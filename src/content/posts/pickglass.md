---
title: Building qualitative research tools using AI.
date: '2026-07-23'
tags:
  - research
description: >-
  Reporting on building two qualitative research tools using AI. These tools
  utilize AI in the building process but also use local LLM models to do some of
  the basic lifting on qualitative research. The aim of these tools is to
  provide an open source open data platform for qualitative research and provide
  a one-stop location for all of the data to facilitate networking.
image: https://res.cloudinary.com/do7oi2ioy/image/upload/v1784991274/casey-site/casey-site/research/QualVis.png
---
![Image](https://res.cloudinary.com/do7oi2ioy/image/upload/v1784991274/casey-site/casey-site/research/QualVis.png)
# From Theme Mapper to PickGlass

This post reports on the development of two tools. The first was Prototyped rapidly to facilitate live qualitative mapping in a workshop session and its first simple instance was a single HTML file for coding workshop insights live, in the room, on a projector.This was enhanced later to build in the capability for first-pass qualitative analysis by a small LLM model running locally and also an improved cross-tab feature to allow for more detailed data analysis. 

The second is a desktop application for carrying an entire qualitative design-research study — sources, codes, insights, memos, literature, and the final write-up — in a folder of plain markdown files.

The second grew out of the first to some degree but also out of my experience of using Obsidian combined with Jupyter notebooks to capture and analyze qualitative data [Qualatative Analysis with Jupyter](2023-05-21-qualitative-analysis-with-jupyter.md). Both grew out of the same desire to have qualitative analysis tools that fit well with the manner in which design research actually unfolds, but also copes  with the sprawl of data that qualitative analysis can generate while keeping open formats and not locking the research data behind expensive commercial software and proprietary file formats.

## The workshop problem

Design has a propensity to action. Design research data often arises in dynamic situations such as  workshops, co-design sessions or crit walls. These are moments where insights are voice, frequently captured on stickies and too often die in a photograph of a whiteboard that rapidly looses context over time. Design research is also iterative in nature with one research interaction frequently influencing the design and execution of the next. 

The conventional manual approaches to tools for qualitative analysis and software tools such as NVivo, ATLAS.ti, MAXQDA assume the analysis happens later, at a desk in a quiet room.

There are frequently situations where the capture and theme insights *during* the session, visibly, so the analysis becomes part of the workshop's shared conversation rather than something done *to* it afterwards when the quality of the insights can fade.

## Theme Mapper: one HTML file, no overhead

Theme Mapper is an attempt to meet that need with a **single, self-contained HTML file**. No install, no backend, no network, no IT-department conversation. Open it in a browser on the facilitator's laptop, plug into the projector, and go.

*[Screenshot: Theme Mapper's capture view — the insight log with theme chips, and the treemap filling as insights are themed]*

The constraint was the design. Because it was one file that ran offline:

- It could be **emailed to a colleague** and just work.
- It could run in rooms with **no wifi and no data-sharing agreement** — which, in university settings, is many rooms.
- Everything lived in the browser's local storage, with JSON snapshots and CSV import/export as the escape hatch.

The application started as a means of producing a treemap and word cloud from codes generated in a faculty strategy session.Through a number of iterations informed by feedback from colleagues the application was developed to provide multi-theme tagging, parent theme groupings, a drill-down treemap, a packed word cloud, a co-occurrence matrix, a cumulative timeline and session filters. To assist with communication of the data the application features a **present mode** that displays visuals for the projector and a projector friendly dark mode.One of the frequent frustrations with commercial software is the difficulty in exporting data and visuals of the analysis the application therefore provides PNG snapshots of every visual, and a codebook export with descriptions, counts and exemplar quotes which is available in HTML and JSON.

*[Screenshot: present mode on a projector — auto-cycling between treemap and word cloud]*

The application allows import and export of csv or JSON files of insight/codes combinations is a very simple human readable file format so that data sets can easily be exported or data sets generated elsewhere can easily be formatted and imported into the tool for visualisation and analysis.

## AI Assistance

Early in the development of the tool one of the core concepts was that the use of a locally running AI model could be of assistance in 1st pass coding of insights to provide rapid feedback to a workshop and prompt reflection and discussion. The tool as presented offers the use of a  **local AI assistance via Ollama**. A model running on the facilitator's own machine can suggest themes from the working codebook, run a review pass for duplicate themes, and bulk-code an imported CSV of raw insights into a drafted codebook. with every suggestion passing through a human review table before anything was applied. The local-first rule was not an aesthetic preference: some workshops operate under data permissions that simply do not allow participant utterances to be sent to a cloud API. A model on your own laptop changes the ethics conversation entirely. That principle — *AI assistance must be local, optional, and reviewable* — carried straight into everything that came after.

*[Screenshot: the AI review table — model-drafted themes awaiting accept/reject]*

## What Theme Mapper couldn't do

Theme Mapper was honest about being a session tool, and its limits taught me exactly what the next tool had to be:

1. **Insights were orphans.** A captured insight had no connection back to a source document — no transcript, no context, no way to ask "what was said around this?"
2. **One session at a time.** A research project is many encounters over months, plus literature, plus memos, plus drafts. Local storage in a browser tab is not a research record.
3. **No path to writing.** The analysis ended at a codebook export. The actual output of research — the written argument with evidence and citations — happened somewhere else, disconnected.
4. **Trust lived in the researcher's memory.** No audit trail, no provenance, nothing an examiner could inspect.

## PickGlass: the vault is the contract

I had already built [ObsLite](2025-12-06-building-obslite.md) — a lightweight, Obsidian-compatible markdown editor in Tauri and Svelte, originally so I could take notes on a Raspberry Pi. That gave the new tool its foundation and its founding principle:

> **The vault format is the contract, not the app.** Everything the researcher produces is a plain markdown file in a folder that opens cleanly in Obsidian or any text editor — and will still open in fifty years. Delete the app; the research survives.

PickGlass (developed under the working name *Loom* until that turned out to clash with existing software) extends ObsLite into a full research workbench:

- **Coding**: select a passage in a transcript, hit ✦ Code, tag it with codes, sentiment and strength, and attach a case. The passage is highlighted in the source — tinted by code, like a marker pen — and the excerpt becomes an **insight note**: an ordinary markdown file carrying the quote, the metadata, and an anchor.

*[Screenshot: coding a transcript passage — the code picker with sentiment/strength and the coloured highlight left behind]*

- **Anchors that heal.** Insights are tied to their source passages by quote-plus-context anchors (the W3C annotation model), not character offsets. Edit the transcript and the anchors re-resolve — exactly, or fuzzily with a confidence score, or flagged as orphaned for a one-click re-pin. Your excerpts survive the inevitable transcript clean-up.

- **The explorer**: Theme Mapper's visuals, reborn over the whole corpus — code treemap, co-occurrence matrix, word cloud — driven by one set of filters (code, sentiment, strength, case, source, free text). Click a matrix cell and read the excerpts behind the pattern before you believe it.

*[Screenshot: the Insights explorer — treemap view with filter chips, then the co-occurrence matrix]*

- **A codebook you calibrate**: descriptions, counts, rename-to-merge across the whole vault, and exports (HTML with exemplar quotes, JSON, CSV) for supervision meetings and for sharing back with participants.

- **Writing with evidence**: draft in markdown, embed any insight as an attributed quotation with `![[insight name]]`, insert literature citations from a picker (❞), and print or export with references resolved — **Harvard by default**, APA one click away. The draft in the vault stays plain wikilinks; styles apply only at output time.

*[Screenshot: a draft in the editor beside its printed PDF — embedded quote rendered with attribution, reference list generated]*

- **Member checking on paper**: print any coded source and the highlights come out tinted by code with a legend — *this is what we heard; did we hear you right?*

*[Screenshot: a printed coded transcript page with the colour legend]*

- **Trustworthiness by construction**: every analytic action — every coding, merge, import, export — lands automatically in an append-only audit trail inside the vault. Lincoln and Guba's dependability criterion, implemented as a file you never have to remember to write.

- **A methods-grounded user guide in every vault**, pairing each feature with the research practice it serves — Braun and Clarke's familiarisation, Saldaña's coding cycles, constant comparison, memoing, the Double Diamond, annotated portfolios, FAIR data — with a quickstart up front.

And the Theme Mapper rule holds: the optional AI assistance (code suggestions from your own codebook) runs against **your own local Ollama**. Nothing leaves your machine, ever.

## How it was built (and what went wrong)

The stack is the ObsLite stack, deliberately boring: Tauri 2 (a thin Rust file-system layer), SvelteKit, CodeMirror 6, marked. All the vault intelligence — indexing, backlinks, anchor resolution, analysis — lives in dependency-free JavaScript modules with their own test suites, so the core logic is portable and provable.

Development was a genuine human–AI collaboration: I set the research requirements, the theory, and the design decisions; Claude wrote most of the code across a series of work packages, with field-testing in between. Some lessons earned the hard way, preserved here for anyone building on similar foundations:

- macOS's WKWebView silently swallows `window.prompt` and `window.confirm` — dialogs must be built in-app.
- The first real PDF export printed an embedded quotation as literal `<blockquote>` source code — the markdown pipeline was escaping its own injected HTML. Field testing catches what unit tests cannot.
- YAML frontmatter must be quoted conservatively, or Obsidian stops parsing your notes.
- And version one of anything looks obvious in hindsight: the print renderer initially reimplemented markdown badly instead of reusing the same renderer as the preview pane. Parity came in v0.8.6, and tables stopped printing as rows of pipe characters.

*[Screenshot: optional — before/after of the PDF rendering fix, if you kept the bad PDF]*

## Try the beta

PickGlass is in early beta — built for my own studies, now looking for a few more hands. Downloads are on the [releases page](https://github.com/Setanta72/PickGlass/releases):

| Platform | File | Note |
|---|---|---|
| macOS (Apple Silicon & Intel) | `.dmg` | Unsigned beta: first launch is **right-click → Open → Open** |
| Windows 10/11 | `-setup.exe` | WebView2 embedded — installs fully offline. SmartScreen: **More info → Run anyway** |
| Linux (x64) | `.AppImage` or `.deb` | AppImage: `chmod +x`, then run |
| Raspberry Pi 4/5 | aarch64 `.AppImage` / `.deb` | Requires 64-bit Pi OS |

First run: create a new vault, open the **PickGlass user guide** that appears at its root, and follow the Quickstart — five moves from empty vault to a printed, evidence-anchored page. If you'd rather build from source, the [README](https://github.com/Setanta72/PickGlass) has the three-command version.

## Feedback

This is a beta, and feedback is the point. Please use [GitHub Issues](https://github.com/Setanta72/PickGlass/issues) — what you did, what you expected, what happened, and your platform. Methodological reactions are as welcome as bug reports: if the tool fights the way you actually analyse, that *is* a bug.

The vault is yours; the app is just a lens on it. That's the whole idea.

---

*Built with Claude assistance — from the first Theme Mapper prototype to the four-platform CI pipeline.*
