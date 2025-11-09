# ASF Incubator Scenario Card & Microlearning Generator

This toolkit converts a **Confluence “View Source” export** of [Practicing The Apache Way](https://cwiki.apache.org/confluence/display/INCUBATOR/Practicing+The+Apache+Way) into both:

- **Printable 2-up duplex scenario cards** for workshops and training  
- **An interactive microlearning course** (Twine/Harlowe format) for self-paced exploration  

---

## Overview

Each scenario in *Practicing The Apache Way* contains:
- A brief summary of a real ASF situation  
- Reflection questions  
- A “Possible Path Forward”

The tools extract and transform this content into reusable learning materials for mentor onboarding, community training, and Incubator workshops.

| Output | Format | Purpose |
|---------|---------|----------|
| **Scenario Cards** | PDF (A4, 2-up duplex) | Printable workshop cards |
| **Microlearning Course** | `.twee` (Harlowe/Twine) | Interactive web or LMS module |

---

## Requirements

- **Python 3.8+**
- Libraries:
  ```bash
  pip install beautifulsoup4 reportlab
  ```
  *(The `microlearning.py` script uses only Python’s standard library.)*

---

## Usage

### 1. Export from Confluence
From the wiki page **Practicing The Apache Way**:
```
••• → View Source
```
Then **save the page source** as:
```
PracticingTheApacheWay.html
```

### 2. Generate scenario cards (PDF)
```bash
python3 generatecards.py --infile PracticingTheApacheWay.html --out scenario_cards.pdf
```

Produces a **2-up duplex PDF** ready for printing double-sided (flip on long edge).

### 3. Generate microlearning course (Twine)
First, run the card generator to produce `cards.json` (optional intermediate step if supported), then:
```bash
python3 microlearning.py --in cards.json --out apache_way_harlowe.twee --images-dir images
```

Outputs a `.twee` file compatible with **Twine**.  
Import it into Twine or publish it as a static HTML course.

---

## Printing Guide (for Cards)

- **Paper size:** A4 landscape  
- **Duplex:** Flip on long edge  
- **Cutting:** Each sheet = two A5 cards  
- **Paper:** 120–160 gsm recommended

---

## File Structure

```
tools/
 ├── generatecards.py               # HTML → 2-up duplex PDF
 ├── microlearning.py               # JSON → Twine (.twee) micro-course
 ├── PracticingTheApacheWay.html    # Confluence export
 ├── cards.json                     # extracted scenarios
 ├── scenario_cards.pdf             # generated printable cards
 └── apache_way_harlowe.twee        # interactive microlearning output
```

---

## How It Works

### `generatecards.py`
1. **Extracts** scenario blocks from Confluence HTML:
   - `<h3>` → scenario title  
   - `<h4>` → sections (“Reflection questions”, “Possible path forward”)  
   - `<p>` / `<ul>` → summaries, lists  
2. **Formats** as JSON and renders to 2-up duplex PDF via ReportLab.

### `microlearning.py`
1. **Reads** `cards.json` and organizes scenarios into thematic groups.  
2. **Generates** a complete `.twee` Twine course:
   - Scenario pages (`Discuss`, `Tips`)  
   - Group summaries and progress tracking  
   - Auto-estimated time per module  
   - Resume and “Finish” gating logic  
3. **Outputs** a ready-to-import `.twee` file for Twine or static hosting.

---

## Troubleshooting

**“No scenarios found”**  
→ Ensure you exported the *View Source* HTML, not the rendered page.  

**PDF misaligned or flipped**  
→ Set duplex printing to *flip on long edge*.  

**Missing images in Twine**  
→ Use `--images-dir` with matching filenames.
