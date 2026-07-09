import ollama #Talk to ollama API program on my computer.

#"response = ollama.chat (  #Send a message to the Mistral AI model and ask it a question and get a response.
 #   model="mistral",
 #   messages=[{"role": "user", "content": "Explain what an AI assistant is in simple terms?"}]
#"")""
#"print(response["message"] ["content"])


# Step 1: load the document
with open("documents/sample.txt", "r") as file:
    document = file.read()

# Step 2: ask a question
#question  = "What is AI according to the document?"
questions  = ["Can AI be used for business purposes according to the document?",
                "What is AI according to the document?"
    ]

# Step 3: send BOTH document + question to AI
response = ollama.chat(
    model="mistral",
    messages=[
        {
            "role": "user",
            "content": f"""
Use ONLY the document below to answer the question.

DOCUMENT:
{document}

QUESTION:
{questions}
"""
        }
    ]
)

# Step 4: print result
print(response["message"]["content"])