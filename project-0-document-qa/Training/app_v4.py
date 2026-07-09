from document_loader import load_document
from titan import ask_titan
from memory import load_memory, save_memory


# Load existing conversation history
history = load_memory()

# Load document knowledge
document = load_document()


print("\nAI Document Assistant (type 'exit' to quit)\n")


while True:

    question = input("Ask a question: ")

    if question.lower() == "exit":
        print("Goodbye 👋")
        break

    # Send document and question to Titan
    answer = ask_titan(document, question, history)

    print("\nAnswer:")
    print(answer)

    # Save conversation history
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