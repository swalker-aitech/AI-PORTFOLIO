import json
import os

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
    Save the conversatin history to disk.
    """
    
    with open(MEMORY_FILE, "w") as file:
        json.dump(history, file, indent=4)
                
