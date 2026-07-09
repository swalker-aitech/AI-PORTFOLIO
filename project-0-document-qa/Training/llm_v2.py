import ollama


def generate_response(history):
    """
    Send the conversation history to the AI
    and return the assistnat's reply.
    """     

    response = ollama.chat(
        ##model"gpt-4.1-mini",
        model="mistral",
        messages=messages

    )

    return response["message"]["content"] 
