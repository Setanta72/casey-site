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

This post reports on the development of two tools. The first was prototyped rapidly to facilitate live qualitative mapping in a workshop session and its first simple instance was a single HTML file for coding workshop insights live, in the room, on a projector. This was enhanced later to build in the capability for first-pass qualitative analysis by a small LLM model running locally and also an improved cross-tab feature to allow for more detailed data analysis.

The second is a desktop application for carrying an entire qualitative design-research study. This includes sources, codes, insights, memos, running notes,literature and the final write-up in one place. All of which exists in a basic folder structure in plain markdown files.

This second application grew out of the first to some degree but also out of my experience of using Obsidian combined with Jupyter notebooks to capture and analyze qualitative data [Qualitative Analysis with Jupyter](2023-05-21-qualitative-analysis-with-jupyter.md). All of these developments Stem from a requirement to have a qualitative analysis tools that fit well with the manner in which design research actually unfolds, but also cope with the sprawl of data that qualitative analysis can generate all the while keeping open formats and not locking the research data behind expensive commercial software and proprietary file formats.These open formats are extremely important when looking at research reuse and the FAIR principles, but also increasingly important as we look at the possibility of using AI as a co-working tool, and these open formats are so much more readily readable and operable with AI tools.

## The workshop problem

Design has a **propensity to action**. Design research data often arises in dynamic situations such as workshops, co-design sessions or crit walls. These are moments where insights are voiced, frequently captured on stickies and then too easily die in a photograph of a whiteboard that rapidly loses context over time. Design research is also iterative in nature with one research interaction frequently influencing the design and execution of the next. This is an aspect that frequently comes under scrutiny with design research when reviewed by other disciplines and therefore is an area where care needs to be taken to provide traceability, an audit trail, and clear demonstration of research rigor.

Both conventional manual approaches to tools for qualitative analysis and software tools such as NVivo, ATLAS.ti, MAXQDA assume the analysis happens later. The normal expectation is that the analysis occurs after all data collection has occurred to control for bias in the study.

Within design research (particularly co-design)there are frequently situations where capturing and theming insights in a highly visable way *during* the session is valuable such that the analysis becomes part of the workshop's shared conversation rather than something done *to* it afterwards when the quality of the insights can fade.

## Theme Mapper: one HTML file, no overhead

Theme Mapper is an attempt to meet that need with a **single, self-contained HTML file**. No install, no backend, no network, no IT-department conversation. Open it in a browser on the facilitator's laptop, plug into the projector, and go.

*[Screenshot: Theme Mapper's capture view — the insight log with theme chips, and the treemap filling as insights are themed]*

Because its a single HTML file it allows the researcher to share both the data and the tool. In this way it empowers collaborators to take multiple views on the data and potentially reduces the load on the workshop facilitator. 

- It can be **emailed to a colleague** and just work.
- It can run in rooms with **no wifi and no data-sharing agreement** which in university settings is many rooms.
- Everything lives in the browser's local storage, with JSON snapshots and CSV import/export to provide a more permanent record and files that can be acted on externally.

The application started as a means of producing a treemap and word cloud from codes generated in a faculty strategy session. Through a number of iterations informed by feedback from colleagues the application was developed to provide multi-theme tagging, parent theme groupings, a drill-down treemap, a packed word cloud, a co-occurrence matrix, a cumulative timeline and session filters. To assist with communication of the data the application features a **present mode** that displays visuals for the projector and a projector friendly dark mode.

*[Screenshot: present mode on a projector — auto-cycling between treemap and word cloud]*

One of the frequent frustrations with commercial software is the difficulty in exporting data and visuals of the analysis. Theme Mapper provides PNG snapshots of every visual, and a codebook export with descriptions, counts and exemplar quotes which is available in HTML and JSON.

*[Screenshot: Image of code book interface]*

The application allows import and export of csv or JSON files of insight/code combinations in a very simple human readable file format. This allows data sets to be exported or data sets generated elsewhere can easily be formatted and imported into the tool for visualisation and analysis.The use of small local LLM tools makes this type of data manipulation quick and easy adding value to the open data formats used. 

## AI Assistance

Early in the development of the tool one of the core concepts was that the use of a locally running AI model could be of assistance in 1st pass coding of insights to provide rapid feedback to a workshop and prompt reflection and discussion. The tool as presented offers the use of **local AI assistance via Ollama**. A model running on the facilitator's own machine can suggest themes from the working codebook, run a review pass for duplicate themes, and bulk-code an imported CSV of raw insights into a drafted codebook. Every suggestion can undergo human review in a table before anything is applied. The use of local models was a key design choice as many workshops operate under data permissions that simply do not allow participant utterances to be sent to a cloud API and there is a lack of clarity regarding ethics for such uses. Having a model on the researchers own computer should allow for more clarity when it comes to ethics approvals and data management. The principle that *AI assistance must be local, optional, and reviewable* carries into future developments.

*[Screenshot: the AI review table — model-drafted themes awaiting accept/reject]*

## Knowing our Limitations: What Theme Mapper couldn't do

I explored expanding the feature set of Theme Mapper but it starts to become unwieldily and drifts too far from its genesis as a light weight session tool. Learning points taken from this tool:

1. **Insights were orphans.** A captured insight had no connection back to a source document. There was no easy way to link the insight to "what was said around this?" That context would need to be provided by narrative notes of the session.
2. **One session at a time.** A research project is many encounters over months, plus literature, plus memos, plus drafts. Local storage in a browser tab is not a research record.
3. **No path to writing.** The analysis ended at a codebook export. The actual output of research — the written argument with evidence and citations — happened somewhere else, disconnected.
4. **Management of continuous data.** The tool is designed around the concept of discreet insights from a workshop. Qualitative research often requires extraction of insights from a non-discrete flow such as an interview. The Theme Mapper tool has no means of managing that type of info within the tool such that a level of traceability can be maintained. 

---

# PickGlass

## What came before it

The development of the PickGlass application emerged from three separate strands of activity that converged and were made possible by the capabilities of AI coding tools (in this case Fable 5).

The recognition of need arose from practice rather than software. As described in the earlier post on [qualitative analysis with Jupyter](2023-05-21-qualitative-analysis-with-jupyter.md) , I had been using [Obsidian as a working environment for qualitative research](2023-04-16-qualitative-analysis-in-obsidian.md) for some time. This PKM managed sources as notes, codes as tags and links, memos as notes about notes, and the backlinks pane serving, informally, as an audit trail. Jupyter notebooks doing the counting and the plotting where numbers were needed. That combination worksand is very powerful but requires a high level of engagement and has more features available than are frequently required leading to distraction and confusion. Obsidian is a massively flexible tool but with that comes an inherent lack of structure. This could lead to a breakdown in consistency over time. Critically Obsidian is [not opensource.](https://obsidian.md/license). It is free but that does not provide the level of long term assurance that an open licence provides.

The second strand was  the development of [**ObsLite**](2025-12-06-building-obslite.md) which was a lightweight, Obsidian-compatible markdown editor written in Tauri and Svelte. This was originally built as a project for the fairly unglamorous reason that I wanted to take notes on a Raspberry Pi in Markdown and the existing options didn't fit the bill for me. It established that a serviceable markdown and vault editor is a relatively modest amount of code. Functionality revolves around a file watcher, and that the vault format which is a folder of markdown files with YAML frontmatter can do most of the work that matters.

The third was Theme Mapper, described above, which provided rapid data visualisation and coding tools. It also whether a small model running locally (Gemma4 12b, via Ollama, on the facilitator's own machine) could contribute usefully to first-pass coding. Its usage within a session with human supervision and review demonstrated the feasibility and potential of this approach. That result may matter less as a technical feature than as a demonstration that the ethics of AI-assisted analysis can be argued on methodological grounds rather than on infrastructural ones. The question of should we use it rather than will it work and what happens to the data.

Running underneath all three is the reservation noted at the outset. Commercial CAQDAS packages offer considerable analytic power but requires that the study lives inside a proprietary project file with a licence and freqiently in a format that cannot be read without the vendor. Version changes and backward compatibility can be an issue. Funding for licence support depend on institutional approvals and are subject to payment and admin delays encountered in large organisations.

For a researcher working over four or five years interested in the long-term stewardship of research data, it is a serious challenge and one the FAIR principles address directly (Wilkinson et al., 2016). These issues can be mitigated with a good data managment plan and clear backup and export protocols but this involves extra steps, risks data degradation and is not open bu default. 

The other obvious alternative is manual analysis usingprinted transcripts, highlighters, the material spread out on a table or board. The immersion that manual coding affords is genuinely difficult to reproduce on a screen but the drawback is this manual analysis does not afford itself to traceability and is difficult to replicate or transport. A table covered in paper cannot be audited and the decisions taken across it are recoverable only from the researcher's memory or require meticulous note taking.

The aim with the PickGlass application was to combine the structure and traceability associated with computer-based analysis with something closer the flexibility of working by hand. Critically this should be done in an open human readable format that no vendor owns. A bonus is that the tool itself is built on an open source stack with all code available so that it can easily be forked and extended. 

## Why the name PickGlass

Qualitative analysis has something in common with weaving. The work begins with loose threads of utterances, observations, images, partly formed hunches and proceeds by working them into a fabric in which warp and weft hold one another in place. A finding is rarely a single thread; it is usually a structure of them. This started the weaving analogy and the early working title was "Loom" but that was (predictably) already taken.

A [**pick glass**](https://en.wikipedia.org/wiki/Pick_glass) is a weaver's instrument: a small folding magnifier laid down on the cloth to count the picks per inch through a window of known size. It is for this analogy both a lens and a measure at the same time with the vault as the cloth and the application as the glass.

## What the tool needed to do

In developing the application requirements were set out before any code was written. These were actually developed in back and forth conversation with Claude based on user insights and each of them rests on a body of methodological literature. They are given here as reasoning rather than as a feature list, since the arguments are the part likely to be useful to someone working with, or selecting, a different tool.

**One place to think.** A study is not only its data. It is meeting notes, supervision notes, a conversation recalled from a corridor, and the daily (contemporaneous) record of what was done and why. Schön (1983) characterised professional knowing as a reflective conversation with the situation in naming what we attend to, framing the problem, making a move, and attending to the situation's back-talk. This kind of interaction happens at least twice in the arc of design research initially with with the design situation and latterly with the data generated. Both need somewhere to be recorded in a manner that they can easily be surfaced and linked. The first requirement was therefore a capability to capture general notes, meeting notes, supervision notes and daily entries should sit in the same searchable and linkable space as the research data, since a reflection that cannot be linked back to whatever provoked it tends to become recollection rather than analysis.

**Data arrives in many forms.** Design research does not generally produce tidy transcripts. It produces a photograph of a whiteboard, a wall of post-its, a page of handwriting from a site visit, an audio note recorded in a car park, a policy document, a sketch. Cross (2006) argued that designerly knowing resides in sketching, making and showing at least as much as in words, and Gaver and Bowers (2012) established the annotated portfolio as a legitimate research output precisely because artefacts and their annotations carry knowledge together. If visual and material evidence is treated as first-class in the epistemology, it should be treated the same way in the tool. Therefore any of these can data become a source, described with metadata, linked with research memos and coded in the same manner as a transcript.

**Notes as the atomic unit.** Simon (1996) characterises design as a science of the artificial, and his account of complexity (1962) holds that systems which survive are nearly decomposable, assembled from stable subassemblies rather than in one continuous sequence. Analysis conducted alongside teaching and supervision is nothing if not interrupted, and the note is the subassembly: an insight, a memo, a reference or a code description, each small enough to be finished in the time actually available and set down without loss. Newell and Simon (1972) supply the corollary that matters most here. A problem space specifies the operators available, not the path a solver takes through them, and the operators in the vault — link, code, describe, merge, memo, embed — carry no commitment as to whether themes are constructed or discovered, or whether coding proceeds inductively or from an a priori framework. Researchers working reflexively and researchers working from a fixed codebook use the same operators and produce vaults of the same shape, differing in the routes they take. Deciding where one insight ends and the next begins is of course already an analytic act; what the vault offers is that the choice is recorded rather than assumed.

**Coding as the capture of meaning.** Krippendorff (2006) argued that design is fundamentally concerned with meaning, in that artefacts succeed or fail according to the meanings stakeholders find in them. This has a direct consequence for coding in design research: a code can be understood as a captured stakeholder meaning, and a codebook as an inventory of the meanings in play. It is a reasonable argument for privileging in-vivo codes, since participants' own words are stakeholder meaning in stakeholder language, and for treating code descriptions as first-class objects rather than as documentation added afterwards. Saldaña (2021) supplies the working rhythm, separating first-cycle coding — descriptive, quick, close to the words — from second-cycle work in which patterns and interpretation have to earn their place. Coding in the first cycle therefore needs to be inexpensive enough to do generously, while the second cycle needs to be a deliberate and visible act.

**Memos with an address.** The emphasis grounded theory places on memoing (Glaser and Strauss, 1967; Charmaz, 2006) is in practice an insistence that analytic thinking be written down while it is still live, and kept somewhere it will be read again. The requirement here was that a memo can be created directly from whatever prompted it — an insight, a source, a reference — and arrives already linked to it. Constant comparison is only workable if the things being compared remain connected to their evidence.

**Literature inside the study rather than beside it.** Most researchers keep their reading in one application and their data in another, and the boundary between the two is where a good deal of abductive reasoning is lost. Dorst (2011) describes design reasoning as a search for the frame that would make observed outcomes possible, and frames come from the literature at least as often as from the data. The requirement was consequently for references imported in batch from BibTeX or RIS, one markdown note per reference, the PDF attachable to that note, reading notes linked to it, and the whole navigable through backlinks in the manner of a Zettelkasten (Ahrens, 2017). A literature note and an insight note being the same kind of object, they can link to one another.

**Writing as part of analysis rather than after it.** The most accessible place to write should be the place in which the evidence already sits. Miles and Huberman (1994) argued that displays drive analysis rather than illustrate it, and something similar applies to drafting. Where reporting happens in a separate application the draft loses its links, quotations are retyped and gradually drift from their sources, and the write-up becomes an exercise of memory. Drafting in the vault, with insights embeddable as attributed quotations and references insertable directly, keeps the final argument continuous with the analysis that produced it.

**Analysis that can be seen, and walked backwards.** This requirement is the most difficult to satisfy honestly. Fielding and Lee (1998) documented a long-running unease that computer-assisted analysis distances researchers from their material, and Braun and Clarke (2019) are emphatic that reflexive thematic analysis is an interpretative craft rather than a procedure to be executed, in that themes are not lying in the data waiting to be located. A tool that dictates a method is therefore of limited use. A tool offering no structure at all, on the other hand, returns you to the table covered in paper. The position taken here is that the tool provides the structures — codes, cases, excerpts, co-occurrence — and declines to provide the procedure. Visualisations are dynamic and remain a click or two from the underlying excerpt, so that a pattern can be read back to the material before it is believed. Grounded, reflexive, framework and template approaches are all workable; the vault is indifferent between them.

**Open formats and an auditable record.** Lincoln and Guba (1985) set out dependability and confirmability as trustworthiness criteria satisfied by an inquiry audit, in which an external reader follows the decision trail. That is not readily achievable where the trail is a proprietary binary and a current licence. Everything in the vault is markdown with YAML frontmatter, readable in any text editor, in Obsidian, or in a file browser, and codebooks and insight tables export as HTML, CSV and JSON for sharing with supervisors, participants and examiners. The FAIR principles are then largely satisfied by construction rather than by additional paperwork.

**One study, one folder.** All the data for a project in a single place, independent of every other project, backed up and transferred by copying a folder. It is a modest requirement with a considerable consequence: handing over a study, whether to a supervisor, an examiner, a collaborator or to oneself some years later, becomes a file transfer rather than a software negotiation.

**AI as an addition, with the question left open.** Theme Mapper demonstrated that a local model can accelerate first-pass coding under supervision. That is not the same as demonstrating that it ought to be used. The methodological literature on generative AI in qualitative analysis is young and contested, and the reflexive traditions raise a substantial objection, namely that the interpretative labour is itself the analysis, so that delegating it risks producing a codebook nobody fully understands. AI assistance in PickGlass is therefore scoped as an optional addition, local only, with human review and an audit entry, and it is an element of the application I have paused implementation on. 

## The vault captures the research

Those requirements produce a single organising principle, from which most of the subsequent decisions follow:

> **The vault format is the contract, not the app.** Everything the researcher produces is a plain markdown file in a folder that opens cleanly in Obsidian or any text editor, and should still open in fifty years. Remove the application and the research remains.

There is a corollary concerning connection. A qualitative design study typically lives in fragments: transcripts in Word, codes in NVivo, memos in a notebook, literature in Zotero, sketches in a camera roll, and the draft in something else again. Each boundary between those containers is a place where a connection can be lost. Further to that context switching has a cognitive overhead and breaks flow. Lost connections are a cause of frustration such as a the memo that never finds its excerpt again, the paper that clearly speaks to a finding but cannot be cited from within the analysis, the workshop photograph separated from the discussion that produced it. Maintaing these connections in your head as a researcher adds to the cognative and emotional labour of qual research so any system that gives **confidence** that information is safe and can easily be found again removes some of this anxiety. 

The approach taken in PickGlass is to make everything a note and every connection a wikilink. A coded excerpt is a note linking to its source, its case and its codes. A memo links to the insights that prompted it. A literature note links to the findings it informs, and through backlinks each of those links is visible from both ends. Reading, note-taking, memoing, coding and writing then cease to be separate activities in separate applications and become a single activity of building a networked dataset, in which the question an examiner or a later self will ask — where did this come from? — is answered by moving backwards through the graph.

*[Screenshot: backlinks pane on an insight note — the memo, the draft and the source that all point at it]*

## A study, moving through the tool

PickGlass, developed under the working name *Loom* until that proved to clash with existing software, extends ObsLite into a research workbench. In roughly the order a study uses it:

- **The daily record.** Notes, meetings, supervision and a dated reflexive journal, all held in the same vault as the data, searchable and linkable to anything else. Familiarisation has somewhere to live before any code is applied.

- **Sources of several kinds.** Interview transcripts, workshop walls, observation notes, documents, and image sources — photographs of whiteboards and post-it walls embedded in a source note whose annotations are themselves codeable. Handwritten field notes can be transcribed by a local model and audio notes transcribed on-device, both arriving as markdown. Each source carries metadata and tags, so the corpus can be filtered by encounter type as well as by content.

*[Screenshot: an image source — whiteboard photograph with coded annotations beneath it]*

- **Coding.** Select a passage in a transcript, apply codes along with sentiment and strength, and attach a case. The passage is highlighted in the source, tinted by code in the manner of a marker pen, and the excerpt becomes an insight note: an ordinary markdown file carrying the quote, the metadata and an anchor. One decision here follows directly from the methods literature. Sentiment and strength attach to the excerpt rather than to the code, because the same code voiced positively by one participant and bitterly by another is not noise, and is frequently the finding.

*[Screenshot: coding a transcript passage — the code picker with sentiment/strength and the coloured highlight left behind]*

- **Anchors that re-resolve.** Insights are tied to their source passages by quote-plus-context anchors, following the W3C annotation model, rather than by character offsets. When a transcript is edited the anchors re-resolve, either exactly, or approximately with a confidence score, or are flagged as orphaned for re-pinning. Excerpts therefore survive the transcript clean-up that is more or less inevitable.

- **Memos** created directly from any insight, source or reference, arriving pre-linked to their evidence and linkable onward to each other.

- **Literature.** Import a single reference or an entire library via BibTeX or RIS. One note per reference, with the PDF attachable, reading notes linked in, and citations insertable into any draft from a picker. Navigation is by link, in the manner of a browser: reference to reading note to insight to memo to draft.

*[Screenshot: a reference note with its attached PDF, reading notes and backlinks from two insights]*

- **The explorer.** Theme Mapper's visuals applied across the whole corpus — code treemap, co-occurrence matrix, word cloud and a dynamic table — driven by a single set of filters covering code, sentiment, strength, case, source and free text. Selecting a matrix cell displays the excerpts behind the pattern.

*[Screenshot: the Insights explorer — treemap view with filter chips, then the co-occurrence matrix]*

- **A codebook that can be calibrated.** Descriptions, counts, rename-to-merge propagating across the whole vault, and exports in HTML with exemplar quotes, JSON and CSV for supervision meetings and for sharing back with participants. The Codes tab is where second-cycle work happens: describing, comparing and merging, with the explorer redrawing as the codebook consolidates.

- **Writing with evidence.** Draft in markdown, embed any insight as an attributed quotation with `![[insight name]]`, insert citations from the picker, export analysis tables and images of the visualisations into the draft, and print or export with references resolved, Harvard by default and APA a click away. The draft in the vault remains plain wikilinks; styles are applied only at output.

*[Screenshot: a draft in the editor beside its printed PDF — embedded quote rendered with attribution, reference list generated]*

- **Member checking on paper.** Any coded source can be printed with its highlights tinted by code and a legend supplied. Returning meanings to the people they came from, and asking whether they were heard correctly, is Krippendorff's semantic turn expressed as a physical gesture, and Sanders and Stappers' (2008) account of participants as partners expressed as a practical obligation.

*[Screenshot: a printed coded transcript page with the colour legend]*

- **Trustworthiness by construction.** Every analytic action — coding, merging, importing, exporting — is recorded automatically in an append-only audit trail held inside the vault. Lincoln and Guba's dependability criterion implemented as a file nobody has to remember to write.

- **A methods-grounded user guide in every vault**, pairing each feature with the research practice it serves — familiarisation, coding cycles, constant comparison, memoing, action-research cycles, the Double Diamond, annotated portfolios and FAIR data — with a quickstart at the front.

## Back to the room

Theme Mapper is not superseded by any of this. A workshop still wants a single HTML file on a projector with no installation and no network, and a study still wants everything gathered into the vault afterwards. Insights therefore move between the two over CSV: out of the vault for a member-checking or presentation session, and back in with whatever the room has changed.

That round trip is built, and it should work, though it has not yet been run under live conditions, which in my experience is the only test that counts. It is first on the list for the next workshop.

## How it was built

The stack is the ObsLite stack and is deliberately unadventurous: Tauri 2 providing a thin Rust layer that reads, writes and watches files, SvelteKit for the interface, CodeMirror 6 for editing, marked for preview, and Ollama as the intended target for the local AI assistance still to come. The vault intelligence — indexing, backlinks, anchor resolution and the analysis mathematics — sits in dependency-free JavaScript modules with their own test suites, so that the core logic is portable and testable independently of any interface.

A few decisions are worth stating explicitly, since each represented a genuine alternative:

- **No database.** The files are the record; the index is rebuilt in the webview at startup and kept current as you work, which is broadly the architecture Obsidian uses. A database would have been faster to query, and would have undermined the founding principle, since the moment research data lives anywhere other than in the files, the files become an export rather than the record.
- **Tauri rather than a native Swift application.** The question was worth asking when the early interface looked plain. The honest answer was that the gap was one of design investment rather than technology: a native rewrite would have meant months regaining parity, the loss of the Raspberry Pi and Windows builds, and the loss of a hot-reload loop that allowed field-tested fixes to ship within minutes. A focused design pass on the web stack achieved the same improvement at a fraction of the cost.
- **Anchors rather than offsets.** Tying excerpts to character positions fails the first time a transcript is edited. Quote-plus-context anchors that re-resolve at read time were built and tested before any interface existed, since a good deal of the rest depends on them.
- **A collection of tools rather than a single tool for everything.** Statistical work belongs in Jupyter, as it did before PickGlass existed, and the insight exports load into pandas in a few lines. Audio transcription and speaker identification live in a separate local application whose markdown output PickGlass imports. Heavy media stays outside the vault behind timestamped observation logs. Plain files serve as the integration layer, which allows each tool to be a good version of one thing.
- **AI at the edges rather than at the centre.** The model suggests, a review table disposes, and the audit trail records. Local operation is a condition rather than a preference, and that constraint, inherited from Theme Mapper, alters the data-permissions conversation with an ethics committee considerably, since nothing leaves the researcher's machine.

Development was a human–AI collaboration in a fairly literal sense: I set the research requirements, the theory and the design decisions, and Claude wrote most of the code across a series of work packages, with field-testing in between. A few lessons were earned the hard way and are recorded here for anyone building on similar foundations:

- macOS's WKWebView silently discards `window.prompt` and `window.confirm`, so dialogs have to be built in-app.
- The first real PDF export printed an embedded quotation as literal `<blockquote>` source, the markdown pipeline having escaped its own injected HTML. Field testing catches what unit tests cannot.
- YAML frontmatter needs to be quoted conservatively or Obsidian stops parsing the notes.
- The print renderer initially reimplemented markdown rather than reusing the renderer already driving the preview pane. Parity arrived in v0.8.6, at which point tables stopped printing as rows of pipe characters.

*[Screenshot: optional — before/after of the PDF rendering fix, if you kept the bad PDF]*

## Try the beta

PickGlass is in early beta. It was built for my own studies and is now at the point where more hands would be useful. Downloads are on the [releases page](https://github.com/Setanta72/PickGlass/releases):

| Platform | File | Note |
|---|---|---|
| macOS (Apple Silicon & Intel) | `.dmg` | Unsigned beta: first launch is **right-click → Open → Open** |
| Windows 10/11 | `-setup.exe` | WebView2 embedded — installs fully offline. SmartScreen: **More info → Run anyway** |
| Linux (x64) | `.AppImage` or `.deb` | AppImage: `chmod +x`, then run |
| Raspberry Pi 4/5 | aarch64 `.AppImage` / `.deb` | Requires 64-bit Pi OS |

On first run, create a new vault and open the PickGlass user guide that appears at its root. The Quickstart runs from an empty vault to a printed, evidence-anchored page in five moves. For building from source, the [README](https://github.com/Setanta72/PickGlass) has the short version.

## Feedback

This is a beta and feedback is the point of publishing it. [GitHub Issues](https://github.com/Setanta72/PickGlass/issues) is the best route — what you did, what you expected, what happened, and your platform. Methodological reactions are as welcome as bug reports: if the tool obstructs the way you actually analyse, that is a bug. If you would rather not use GitHub, [email me](mailto:casey_clan@mac.com) and I will file it.

The vault is yours; the application is a lens on it.

## References

- Ahrens, S. (2017) *How to Take Smart Notes*. North Charleston: CreateSpace.
- Braun, V. and Clarke, V. (2019) 'Reflecting on reflexive thematic analysis', *Qualitative Research in Sport, Exercise and Health*, 11(4).
- Charmaz, K. (2006) *Constructing Grounded Theory*. London: Sage.
- Cross, N. (2006) *Designerly Ways of Knowing*. London: Springer.
- Dorst, K. (2011) 'The core of "design thinking" and its application', *Design Studies*, 32(6).
- Fielding, N. and Lee, R.M. (1998) *Computer Analysis and Qualitative Research*. London: Sage.
- Gaver, W. and Bowers, J. (2012) 'Annotated portfolios', *interactions*, 19(4).
- Glaser, B. and Strauss, A. (1967) *The Discovery of Grounded Theory*. Chicago: Aldine.
- Krippendorff, K. (2006) *The Semantic Turn: A New Foundation for Design*. Boca Raton: CRC Press.
- Lincoln, Y. and Guba, E. (1985) *Naturalistic Inquiry*. Beverly Hills: Sage.
- Miles, M.B. and Huberman, A.M. (1994) *Qualitative Data Analysis: An Expanded Sourcebook*. 2nd edn. Thousand Oaks: Sage.
- Saldaña, J. (2021) *The Coding Manual for Qualitative Researchers*. 4th edn. London: Sage.
- Sanders, E.B.-N. and Stappers, P.J. (2008) 'Co-creation and the new landscapes of design', *CoDesign*, 4(1).
- Schön, D. (1983) *The Reflective Practitioner: How Professionals Think in Action*. New York: Basic Books.
- Wilkinson, M.D. et al. (2016) 'The FAIR Guiding Principles for scientific data management and stewardship', *Scientific Data*, 3.

---

*Built with Claude assistance — from the first Theme Mapper prototype to the four-platform CI pipeline.*
