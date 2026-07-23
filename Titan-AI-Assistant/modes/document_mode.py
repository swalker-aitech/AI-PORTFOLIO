from document_loader import load_document
from document_manager import list_documents
from chunker import create_chunks
from core.conversation import start_conversation


def run_document_mode():

    documents = list_documents()

    print("\nAvailable Documents:\n")

    for i, filename in enumerate(documents, start=1):
        print(f"{i}. {filename}")


    while True:

        try:

            choice = int(input("\nSelect a document: "))

            if choice < 1 or choice > len(documents):
                print("Invalid document selection.")
                continue

            selected = documents[choice - 1]
            break

        except ValueError:

            print("Please enter a document number.")


    document = load_document(selected)

    print("\n--- DOCUMENT PREVIEW ---")
    print(document[:500])
    print("--- END PREVIEW ---\n")


    chunks = create_chunks(document)

    print(f"\nDocument split into {len(chunks)} chunks.\n")


    start_conversation(
        document=document,
        mode="document"
    )