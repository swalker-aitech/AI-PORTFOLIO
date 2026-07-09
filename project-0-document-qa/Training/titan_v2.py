##import ollama
from prompts import STRICT_DOCUMENT_PROMPT
from llm import generate_response

def ask_titan(document, question, history
    """
    Build Titan's message and request an answer.
    """
    messages = [
            {
                "role": "system",
                "content": STRICT_DOCUMENT_PROMPT
            },
            {
                "role": "user",
                "content": f"""
DOCUMENT:
{document}

HISTORY:
{history}

QUESTION:
{question}
""" 
        }
    ]
    
    print(messages)

    return generate_response(messages)
