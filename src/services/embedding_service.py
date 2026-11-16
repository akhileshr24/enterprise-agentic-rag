from sentence_transformers import SentenceTransformer

from src.core.config import settings


model = SentenceTransformer(settings.EMBEDDING_MODEL_BASE)


def generate_embeddings(texts):
    embeddings = model.encode(texts)

    return embeddings.tolist()