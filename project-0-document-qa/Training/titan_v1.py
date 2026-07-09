import ollama
from prompts import STRICT_DOCUMENT_PROMPT

def ask_titan(document, question):
    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role": "system",
                "content": STRICT_DOCUMENT_PROMPT
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

    return response["message"]["content"]
