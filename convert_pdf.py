# docling conversion
from docling.document_converter import DocumentConverter

converter = DocumentConverter()

result = converter.convert(
    "sample.pdf"
)

markdown = result.document.export_to_markdown()

with open("sample.md", "w", encoding="utf-8") as f:
    f.write(markdown)

print("PDF converted successfully!")