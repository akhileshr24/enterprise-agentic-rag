from src.services.chunk_service import chunk_documents


def test_chunk_documents():
    documents = [
        {
            "text": "Abc" * 2500,
            "metadata": {"source": "test.pdf", "page": 1}
        }
    ]

    chunks = chunk_documents(documents)

    assert len(chunks) == 10
    assert len(chunks[0]["text"]) == 1000
    assert chunks[0]["metadata"]["source"] == "test.pdf"