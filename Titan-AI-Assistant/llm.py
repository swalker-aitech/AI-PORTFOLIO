import ollama


def generate_response(messages):

    response = ollama.chat(
        model="mistral",
        messages=messages
    )

    return response["message"]["content"]