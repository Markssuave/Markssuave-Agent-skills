---
name: markitdown
description: >-
  Alias for /doc-markitdown to convert Office docs and PDFs into Markdown.
---

<what-to-do>

## Objective
Convert binary files, office documents, slide decks, spreadsheets, and media into clean, structured Markdown text. Use this skill whenever you need to inspect, ingest, or extract content from non-text files for analysis, documentation, or LLM context ingestion.

## Supported Formats
- **Documents**: PDF (`.pdf`), Microsoft Word (`.docx`)
- **Presentations**: Microsoft PowerPoint (`.pptx`)
- **Spreadsheets**: Microsoft Excel (`.xlsx`), CSV (`.csv`)
- **Web & Structured Data**: HTML (`.html`), JSON (`.json`), XML (`.xml`)
- **Audio / Media**: Audio speech files (`.mp3`, `.wav`) transcribed to Markdown text

---

## Execution Instructions

### 1. Command-Line Invocation (Preferred)
To convert a file and save it directly to a Markdown target:
```powershell
python -m markitdown "path/to/document.pdf" -o "path/to/output.md"
```

To pipe or stream the converted Markdown directly for immediate reading:
```powershell
python -m markitdown "path/to/document.docx"
```

### 2. Python Script API (For In-Memory Processing)
When writing one-off scripts in scratch folders or automated pipelines:
```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("path/to/spreadsheet.xlsx")

# Access the structured text content
markdown_text = result.text_content
print(markdown_text)
```

### 3. Agent Ingestion Workflow
When a user asks you to review or analyze a non-markdown file:
1. Locate the source file in the workspace.
2. Run `python -m markitdown "<input_file>" -o "<output_file>.md"`.
3. Read the generated `.md` file using `read_file`.
4. Proceed with the user's analytical, code generation, or review task.

---

## Output Quality Rules
- **Tables**: Ensure tabular data from Excel or Word is rendered as clean GitHub Flavored Markdown (GFM) pipe tables.
- **Headings**: Validate that document hierarchy (H1 -> H2 -> H3) matches the original document structure.
- **Formulas**: Keep raw formulas or numerical values intact without truncation.

</what-to-do>

<supporting-info>

## Troubleshooting & Dependencies

- **Missing Package**: If `markitdown` is not found in the environment, install it via:
  ```powershell
  python -m pip install markitdown
  ```
- **OCR / Image Extraction**: For complex scanned PDFs with image text, configure an LLM client or Azure Document Intelligence plugin:
  ```python
  from markitdown import MarkItDown
  from openai import OpenAI

  client = OpenAI()
  md = MarkItDown(llm_client=client, llm_model="gpt-4o")
  result = md.convert("scanned_receipt.jpg")
  ```

</supporting-info>
