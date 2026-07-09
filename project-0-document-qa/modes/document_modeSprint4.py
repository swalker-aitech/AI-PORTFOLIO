from document_loader import load_document
from titan import ask_titan
from memory import load_memory, save_memory


def run_document_mode():

    history = load_memory()

    document = load_document()

    print("\nAI Document Assistant (type 'exit' to quit)\n")

    while True:

        question = input("Ask a question: ")

        if question.lower() == "exit":
            print("Goodbye 👋")
            break

        ##answer = ask_titan(document, question, history)

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