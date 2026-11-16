from src.services.pdf_service import load_pdf


def test_load_real_pdf():
    documents = load_pdf("data/pdfs/test.pdf")

    # PDF should contain extractable text
    assert len(documents) > 0

    # First extracted document should contain text
    assert documents[0]["text"]

    # Check source filename
    assert documents[0]["metadata"]["source"] == "test.pdf"

    # Check original PDF page number
    assert documents[0]["metadata"]["page"] >= 1

    # Check all extracted pages have valid metadata
    for document in documents:
        assert document["text"]
        assert document["metadata"]["source"] == "test.pdf"
        assert document["metadata"]["page"] >= 1