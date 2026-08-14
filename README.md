# PlannerSuites

Flowchart diagramming, 3D construction simulation, and an idea board — in one place, to make planning more accessible.

Everything runs **entirely in the browser**. No install, no server, no account, no data leaves your machine.

## The tools

| Tool | File | What it does |
|------|------|--------------|
| 🏠 **Home** | `construction-planner/home.html` | Portal linking all three tools |
| 🔷 **FlowForge** | `construction-planner/flowchart.html` | Visio-style flowchart maker |
| 🧩 **IdeaBoard** | `construction-planner/whiteboard.html` | Miro/Jamboard-style infinite whiteboard |
| 🏗️ **ConstructSim** | `construction-planner/index.html` | 3D construction methodology planner |

### 🔷 FlowForge — flowchart maker
- Standard flowchart stencils (process, decision, terminator, document, multidocument, database, predefined process, manual input/operation, merge, on/off-page reference, preparation, delay…) plus basic shapes and containers
- Smart connectors: hover a shape's edge dots to draw links, drag endpoints to re-route, draggable elbows, straight/curved/orthogonal styles, arrowheads and labels
- **Multi-page tabs**, **autosave**, **smart alignment guides**, **group/ungroup**, **format painter**, **shape search**, **templates**, **dark mode**
- Text: fonts (incl. Arial Narrow), sizes, colours, bullets with indent levels (Tab / Shift+Tab), and Word-style alignment
- Export to **PNG / SVG** with a preview dialog (area, scale, background, padding), save/open as `.flow`

### 🧩 IdeaBoard — infinite whiteboard
- Sticky notes, freehand pen, highlighter, eraser
- Shapes, lines, arrows, text, images (drag-drop or paste)
- Infinite pan/zoom canvas, multi-select, undo/redo, export PNG, save/open as `.board`

### 🏗️ ConstructSim — 3D planner
- Model walls, slabs, columns, beams, footings, stairs, scaffolding and formwork across levels
- Phase-based build sequencing with a timeline, snapshots, and project save/load

## Getting started

Just open the file — no build step:

```bash
git clone https://github.com/ihzaa-H/PlannerSuites.git
```

Then double-click `construction-planner/home.html`.

### Portable single file
`construction-planner/FlowForge (portable).html` is the whole flowchart maker in one self-contained file — email it, put it on a USB stick, open it anywhere.

### Desktop app (optional)
An Electron wrapper is included:

```bash
cd construction-planner
```
```bash
npm install
```
```bash
npm start
```

Build a Windows installer with `npm run dist`.

## Publishing changes

The site is live at **https://ihzaa-h.github.io/PlannerSuites/** and redeploys
automatically on every push to `main`.

GitHub Pages serves pages with a fixed `Cache-Control: max-age=600` and does not
allow custom headers, so browsers can hold a stale copy after a deploy. To avoid
that, every page carries a build id and compares it against `version.json` on
load, reloading itself once if a newer build is live.

Before committing a change you want people to see, refresh the build id:

```bash
python scripts/stamp_build.py
```

Then commit and push as usual. (Stamping happens at commit time rather than in
the workflow because GitHub also runs its own `pages-build-deployment` builder,
which publishes the raw repository content and would overwrite a build-time
stamp.)

## Repository layout

```
construction-planner/     the apps
  home.html               portal
  flowchart.html          FlowForge
  whiteboard.html         IdeaBoard
  index.html              ConstructSim 3D
  assets/                 icons
  lib/                    three.js and loaders
Saved Files/              your diagrams, boards and exports
```

`node_modules/` and `dist/` are not committed — regenerate them with `npm install` and `npm run dist`.

## License

MIT
