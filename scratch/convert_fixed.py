import sys
import os
from pathlib import Path

# Add markitdown src to path
sys.path.append(r"e:\markitdown\packages\markitdown\src")

from markitdown import MarkItDown

def convert_pdf(pdf_path, output_path):
    md = MarkItDown()
    try:
        result = md.convert(pdf_path)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(result.text_content)
        print(f"Successfully converted {pdf_path} to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    pdf_file = r"C:\Users\x1 carbon\Downloads\vnd_shareholder_report.pdf"
    output_file = r"e:\markitdown\shareholder_report_fixed.md"
    convert_pdf(pdf_file, output_file)
