#document analysis
from llm import generate_response


def summarize_document(document):

    prompt = f"""
Summarize the following document.

The summary should:
- Be concise
- Include the main purpose
- Mention important topics
- Do not invent information

DOCUMENT:

{document}
"""

    return generate_response(prompt)