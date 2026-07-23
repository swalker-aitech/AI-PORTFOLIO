from titan import ask_titan
from memory import load_memory, save_memory
from commands import process_command


def start_conversation(
        document="",
        mode="general"
):
    """
    Shared Titan conversation engine.

    Handles:
    - user input
    - exit command
    - Titan commands
    - LLM requests
    - memory storage
    """

    history = load_memory()

    print("\nTitan Conversation Started (type 'exit' to quit)\n")


    while True:

        question = input("\nAsk a question (type 'help' for commands): ").strip()

        if question.lower() == "help":
            print("""
Available Commands
------------------
help      - Show this menu
version   - Show Titan version
history   - Show conversation history
clear     - Show conversation history
exit      - Quit Titan
""")
            continue

        if question.lower() == "exit":
            print("Goodbye 👋")
            break

        handled, response = process_command(question)

        if handled:
            print(f"\n{response}\n")
            continue

        answer = ask_titan(
            document,
            question,
            history,
            mode=mode
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
