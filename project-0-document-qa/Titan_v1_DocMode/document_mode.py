from titan import ask_titan
from document_loader import load_document
from memory import load_history, save_history


def run_document_mode():
    #print("Document Mode selected.")
    print("\nAI Document Assistant (type 'exit' to quit)")

    while True:
        question = input("\nAsk a question: ")

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

    # load document

    # conversation loop

    # call titan

    # print answer