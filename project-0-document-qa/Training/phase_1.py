import ollama
from document_loader import load_document
from titan import ask_titan

# Load document once

    #with open("documents/sample.txt", "r") as file:
    #document = file.read()
document = load_document()
print("\nAI Document Assistant (type 'exit' to quit)\n")


while True:
    question = input("Ask a question: ")

    if question.lower() == "exit":
        print("Goodbye 👋")
        break

    response = ask_titan(document, question)

    print("\nAnswer:")
    #print(response["message"]["content"])
    answer = ask_titan(document, question)
    print(answer)
    print("\n" + "-" * 40 + "\n")
   