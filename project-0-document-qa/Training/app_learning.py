import ollama
from document_loader import load_document
vrom titan import ask_titan

# Load document once

    #with open("documents/sample.txt", "r") as file:
    #document = file.read()
document = load_document()
print("\nAI Document Assistant (type 'exit' to quit)\n")

SYSTEM_RULES = """
You are a strict document-based AI assistant.

Rules:
1. Only use the provided document to answer questions.
2. If the answer is not in the document, say: "Not found in document."
3. Do NOT assume or add outside knowledge.
4. Keep answers clear and concise.
5. If a question is ambiguous, ask for clarification instead of guessing.
"""

while True:
    question = input("Ask a question: ")

    if question.lower() == "exit":
        print("Goodbye 👋")
        break

    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_RULES
            },
            {
                "role": "user",
                "content": f"""
DOCUMENT:
{document}

QUESTION:
{question}
"""
            }
        ]
    )

    print("\nAnswer:")
    print(response["message"]["content"])
    print("\n" + "-" * 40 + "\n")