![Python](https://img.shields.io/badge/Python-3.14.3-blue.svg?style=for-the-badge&labelColor=101418&color=9ccbfb)
![Ollama](https://img.shields.io/badge/LLM-Ollama-black.svg?style=for-the-badge&labelColor=101418&color=b9c8da)
![Status](https://img.shields.io/badge/Status-Experimental-orange.svg?style=for-the-badge&labelColor=101418&color=F3C27C)
![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen.svg?style=for-the-badge&labelColor=101418&color=9AF47C)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-blue.svg?style=for-the-badge&labelColor=101418&color=9ccbfb)


<h1 align=center>AutoDraft</h1>

![GitHub last commit](https://img.shields.io/github/last-commit/kingsiddhu/Apply-Buddy?style=for-the-badge&labelColor=101418&color=9ccbfb)
[![GitHub Repo stars](https://img.shields.io/github/stars/kingsiddhu/Apply-Buddy?style=for-the-badge&labelColor=101418&color=EAF47B)](https://github.com/kingsiddhu/Apply-Buddy/stargazers)
![GitHub forks](https://img.shields.io/github/forks/kingsiddhu/Apply-Buddy?style=for-the-badge&labelColor=101418&color=F3C27C)
![GitHub repo size](https://img.shields.io/github/repo-size/kingsiddhu/Apply-Buddy?style=for-the-badge&labelColor=101418&color=d3bfe6)
![GitHub watchers](https://img.shields.io/github/watchers/kingsiddhu/Apply-Buddy?style=for-the-badge&labelColor=101418&color=b9c8da)
![GitHub issues](https://img.shields.io/github/issues/kingsiddhu/Apply-Buddy?style=for-the-badge&labelColor=101418&color=9AF47C)

<p align=center>If you like this project, consider giving it a ⭐</p>


## Overview

AutoDraft is an AI-powered document generation pipeline built around LaTeX templates.

Instead of manually editing the same document repeatedly (emails, reports, contracts, forms), AutoDraft extracts information from a webpage (or a custom source), lets an LLM determine what belongs in each placeholder, inserts the content into a LaTeX template, and generates a final PDF draft.

The system also supports traditional placeholder replacement without AI if desired.

AutoDraft can either:
- Fill placeholders manually
- Automatically fill templates using an LLM and prior given information
- Scrape information directly from webpages (large databases, wikipidia, etc.)
- Compile the finished document into a PDF using a local or remote LaTeX server

WIP
PS. I have decided to make the code a lot more readable and friendly to work with. Hadn't had the habit of it.

## Tech Stack

- **Language:** Python
- **Core Libraries:**

  - `langgraph`
  - `langchain-ollama`
  - `playwright`
  - `beautifulsoup4`
  - `requests`
  - `langgraph`

## Features

- AI-assisted document generation
- Manual placeholder replacement
- RAG-based context retrieval
- Automatic webpage scraping
- Configurable website parsers
- Remote or local LaTeX compilation
- Markdown-based reusable content system
- Automatic PDF generation
- Multiple LaTeX compiler support
- Fallback between multiple LaTeX servers

## Installation

## 1. Install Python

Python 3.11+ recommended.

## 2. Clone the Repository

```bash
git clone https://github.com/kingsiddhu/AutoDraft.git

cd AutoDraft
```

---

## 3. Create Virtual Environment

```bash
python -m venv venv
```

Linux / macOS

```bash
source venv/bin/activate
```
Windows
```powershell
venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Install Ollama

Download:

https://ollama.com

Verify:

```bash
ollama --version
```

---

## 6. Download Required Model

Current default:

```bash
ollama pull qwen2.5:7b
```

Start Ollama:

```bash
ollama serve
```

---

## 7. Install Playwright Browsers

```bash
playwright install
```

---

## 8. Authentication (Optional)

Some websites require login.

Login once using Playwright and save the browser state as

```
./auth.json
```

AutoDraft will automatically reuse this session for scraping authenticated pages.




# Creating Templates

Templates are ordinary `.tex` files.

Placeholders use the following syntax:

```latex
Dear [[company]],

I am excited to apply for the [[position]] role.

[[body]]

Kind regards,

[[name]]
```

AutoDraft automatically detects every placeholder.

---

# Markdown Content Library

Each template may have a matching Markdown file from which the AI can derive context from or use the Headings as placeholders to replace with the preset choices.

Example:

```md
# teamwork

- Collaborated with engineers across departments.
- Worked in agile development environments.

# backend

- Developed REST APIs using FastAPI.
- Designed scalable backend systems.
```

The AI selects the most relevant section and inserts one of its bullet points into the template.

---

# Website Configurations

Website parsers live inside

```
Settings/
```

Each website has its own JSON configuration describing where information should be extracted.

Example:

```json
{
    "PLACEHOLDER 1":"class-name",
    "Placeholder 2":"class-name-2",
    "description":"job-description",
    "tags": ["section", "Primary content"]
}
```
(tags are used for non class elements given example: html block "section" with aria-label as "Primary content")

This allows different websites to be scraped without modifying the source code.

---

# LaTeX Server

AutoDraft supports multiple compilation servers.

Example:

```python
candidate_servers = [
    "http://localhost:8080",
    "https://my-ngrok-server.ngrok-free.app",
    "https://latex.ytotech.com"
]
```

The first reachable server is automatically selected.

---

# Usage

Run:

```bash
python app.py
```

You will be prompted for a webpage URL.

Example:

```
Enter Link to scrape:
```

AutoDraft will

1. Download the webpage
2. Extract relevant information
3. Ask the LLM to fill placeholders
4. Allow manual editing if needed
5. Compile the LaTeX template
6. Generate the PDF

The finished document is saved as

```
testing.pdf
```

---

# Adding New Templates

Simply add three files to the `Data/` folder.

Example:

```
Template.tex
Template.md   (optional)
Template.json (additional data to send to the Latex Server to compile)
```

The program automatically discovers available templates.

---

# Notes

- The AI output is intended to accelerate document creation and should be reviewed before submission.
- Some websites may require authentication.
- LaTeX compilation depends on the availability of a working server.
- This project is still under active development.

---

# Future Improvements

- GUI/Desktop application
- Web interface
- Multiple template selection
- Better RAG pipeline
- Multi-document generation
- Streaming PDF previews
- Batch document generation
- Support for DOCX export


## Authors:

- [Siddharth](https://github.com/kingsiddhu)

## Star History


<a href="https://www.star-history.com/?repos=kingsiddhu%2FAutoDraft&type=timeline&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=kingsiddhu/AutoDraft&type=timeline&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=kingsiddhu/AutoDraft&type=timeline&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=kingsiddhu/AutoDraft&type=timeline&legend=top-left" />
 </picture>
</a>