import ollama

# Load document once
with open("documents/sample.txt", "r") as file:
    document = file.read()

print("\nAI Document Assistant Ready (type 'exit' to quit)\n")

while True:
    question = input("Ask a question: ")

    if question.lower() == "exit":
        print("Goodbye 👋")
        break

    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role": "user",
                "content": f"""
Use ONLY the document below to answer.

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
    print("\n" + "-"*40 + "\n")