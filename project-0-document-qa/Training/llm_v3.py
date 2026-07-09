import ollama

def generate_response(messages):
    print("LLM received:")
    print(messages)

    response = ollama.chat(
        model="mistral",
        messages=messages
    )

    return response["message"]["content"]