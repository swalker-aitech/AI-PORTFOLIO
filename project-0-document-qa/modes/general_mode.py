from titan import ask_titan
from memory import load_memory, save_memory


def run_general_mode():

    history = load_memory()

    print("\nAI General Assistant (type 'exit' to quit)\n")

    while True:

        question = input("Ask a question: ")

        if question.lower() == "exit":
            print("Goodbye 👋")
            break

        answer = ask_titan(
            "",
            question,
            history,
            mode="general"
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