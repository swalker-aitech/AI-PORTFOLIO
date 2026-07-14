def create_chunks(document_text):
    """
    Splits documents into chunks.

    Uses requirement-based chunking when possible.
    Falls back to paragraph chunking.
    """

    # Requirement-based documents
    if "Requirement " in document_text:

        chunks = document_text.split("Requirement ")

        chunks = chunks[1:]

        chunks = [
            "Requirement " + chunk.strip()
            for chunk in chunks
        ]

        return chunks

    # General document fallback
    else:

        chunks = document_text.split("\n")

        chunks = [
            chunk.strip()
            for chunk in chunks
            if chunk.strip()
        ]

        return chunks