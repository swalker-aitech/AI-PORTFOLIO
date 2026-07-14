import json
import os
from datetime import datetime


MEMORY_FILE = "conversation_history.json"


def load_memory():
    """
    Load the conversation history from disk.
    Returns an empty list if no history exists.
    """

    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as file:
        return json.load(file)


def save_memory(history):
    """
    Save the conversation history to disk.
    Adds timestamps for debugging and traceability.
    """

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if history:
        history[-1]["timestamp"] = timestamp

    with open(MEMORY_FILE, "w") as file:
        json.dump(history, file, indent=4)

def get_history():
    """
    Return the full conversation history.
    """
    return load_memory()


def get_last_question():
    """
    Return the most recent question.
    """
    history = load_memory()

    for item in reversed(history):

        if item["role"] == "user":
            return item["content"]

    return None


def clear_history():
    """
    Clear all conversation history.
    """
    save_memory([])