from src.services.embedding_service import generate_embeddings


def test_generate_embeddings():
    texts = [
        "Python is used for AI.",
        "FastAPI is a Python framework."
    ]

    vectors = generate_embeddings(texts)

    assert len(vectors) == 2
    assert len(vectors[0]) == 768
    assert len(vectors[1]) == 768