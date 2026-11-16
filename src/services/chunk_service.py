def chunk_documents(documents, chunk_size=1000, overlap=200):
    chunks = []

    for document in documents:
        text = document["text"]
        start = 0

        while start < len(text):
            end = start + chunk_size

            chunks.append({
                "text": text[start:end],
                "metadata": document["metadata"]
            })

            start += chunk_size - overlap

    return chunks