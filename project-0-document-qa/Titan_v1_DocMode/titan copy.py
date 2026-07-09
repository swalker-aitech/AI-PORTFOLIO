from prompts import STRICT_DOCUMENT_PROMPT
from llm import generate_response


def ask_titan(document, question, history):
    """
    Build Titan's context and request an answer.
    """

    history_text = ""

    for item in history:
        history_text += f"{item['role'].capitalize()}: {item['content']}\n"

    messages = [
        {
            "role": "system",
            "content": STRICT_DOCUMENT_PROMPT
        },
        {
            "role": "user",
            "content": f"""
PREVIOUS CONVERSATION:
{history_text}

DOCUMENT:
{document}

QUESTION:
{question}
"""
        }
    ]

    return generate_response(messages)