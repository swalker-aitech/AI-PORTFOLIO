# document_manager.py
import os


def list_documents(folder="documents"):
    """
    Returns a list of PDF files in the documents folder.
    """

    if not os.path.exists(folder):
        return []

    return [
        file
        for file in os.listdir(folder)
        if file.lower().endswith((".txt", ".pdf"))
    ]