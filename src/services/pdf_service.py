import pymupdf
from pathlib import Path


def load_pdf(file_path: str) -> list[dict]:
    documents = []
    pdf_path = Path(file_path)

    with pymupdf.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf, start=1):
            text = page.get_text("text").strip()

            if text:
                documents.append({
                    "text": text,
                    "metadata": {
                        "source": pdf_path.name,
                        "page": page_number
                    }
                })

    return documents