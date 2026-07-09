from prompts import STRICT_DOCUMENT_PROMPT, GENERAL_CHAT_PROMPT
from llm import generate_response


def ask_titan(document, question, history, mode="document"):
    """
    Build Titan's context and request an answer.
    """

    if mode == "document":
        system_prompt = STRICT_DOCUMENT_PROMPT

    elif mode == "general":
        system_prompt = GENERAL_CHAT_PROMPT

    else:
        system_prompt = STRICT_DOCUMENT_PROMPT

    history_text = ""

    for item in history:
        history_text += f"{item['role'].capitalize()}: {item['content']}\n"

    messages = [
        {
            "role": "system",
            "content": system_prompt
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