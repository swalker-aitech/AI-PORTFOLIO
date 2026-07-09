from document_loader import load_document
from titan import ask_titan
from memory import load_memory, save_memory
from document_manager import list_documents


def run_document_mode():

    history = load_memory()

    documents = list_documents()

    print("\nAvailable Documents:\n")

    for i, filename in enumerate(documents, start=1):
        print(f"{i}. {filename}")

    choice = int(input("\nSelect a document: "))

    selected = documents[choice - 1]

    document = load_document(selected)

    print("\nAI Document Assistant (type 'exit' to quit)\n")

    while True:

        question = input("Ask a question: ")

        if question.lower() == "exit":
            print("Goodbye 👋")
            break

        answer = ask_titan(
            document,
            question,
            history,
            mode="document"
        )

        print("\nAnswer:")
        print(answer)

        history.append(
            {
                "role": "user",
                "content": question
            }
        )

        history.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        save_memory(history)

        print("\n" + "-" * 40 + "\n")