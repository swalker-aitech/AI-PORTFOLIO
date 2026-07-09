from document_loader import load_document
from titan import ask_titan
from memory import load_memory, save_memory
from modes.document_mode import run_document_mode
from modes.general_mode import run_general_mode

##run_document_mode() These are temporary calls.
##run_general_mode()

"""mode = input(
    "\nSelect mode:\n"
    "1. Document Mode\n"
    "2. General Chat\n\n"
    "Choice: "
)

if mode == "1":
    run_document_mode()

elif mode == "2":
    run_general_mode()

else:
    print("Invalid selection.")
"""

mode = input(
    "\nSelect mode:\n"
    "1. Document Mode\n"
    "2. General Chat\n\n"
    "Choice: "
)

if mode == "1":
    run_document_mode()

elif mode == "2":
    run_general_mode()

else:
    print("Invalid selection.")

history = load_memory()

document = load_document()

print("\nAI Document Assistant (type 'exit' to quit)\n")

while True:

    question = input("Ask a question: ")

    if question.lower() == "exit":
        print("Goodbye 👋")
        break

    answer = ask_titan(document, question, history)

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

