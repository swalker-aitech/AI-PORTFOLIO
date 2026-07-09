from titan import ask_titan

document = "Titan is an AI assistant project built with Python."

question = "What is Titan?"

answer = ask_titan(document, question)

print("\nTitan Response:")
print(answer) 