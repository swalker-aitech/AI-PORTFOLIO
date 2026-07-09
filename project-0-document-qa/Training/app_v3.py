#import ollama
from document_loader import load_document
from titan import ask_titan
from memory import load_memory, save_memory
#from llm import generate_response

history = load_memory()
document = load_document()

user_message = input("You: ")

response = generate_response(history)


# Load document once

    #with open("documents/sample.txt", "r") as file:
    #document = file.read()
document = load_document()
conversation_history = []
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


    
    conversation_history.append(f"User: {question}")
    conversation_history.append(f"Assistant: {answer}")    

for item in conversation_history:
        #print(item)
        
        print("\nConversation History")
        print("--------------------")

for item in conversation_history:
    print(item)
    print("--------------------\n")
   
    print("\n" + "-" * 40 + "\n")
   