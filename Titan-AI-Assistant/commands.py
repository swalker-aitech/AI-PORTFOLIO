"""
commands.py

Titan Command Processor

Handles built-in commands before requests are sent
to the document intelligence engine.
"""
import string

from memory import (
    get_history,
    get_last_question,
    clear_history
)


def process_command(question):
    """
    Process built-in Titan commands.

    Returns:
        (True, response)   -> command handled
        (False, None)      -> not a command
    """

    #q = question.lower().strip().replace("?", "")
    q = question.lower().strip()
    q = q.translate(str.maketrans("", "", string.punctuation))

    command_map = {
        "help": help_command,
        "commands": help_command,

        "last question": last_question,
        "what was my last question": last_question,
        "what was the last question": last_question,

        "history": conversation_history,
        "show history": conversation_history,
        "conversation history": conversation_history,

        "clear memory": clear_memory,
        "clear history": clear_memory,

        "question count": question_count,
        "how many questions have i asked": question_count,
    }

    if q in command_map:
        return True, command_map[q]()

    return False, None

def last_question():

    last = get_last_question()

    if last:
        return f"Previous question:\n{last}"

    return "No previous question found."

def conversation_history():

    history = get_history()

    if not history:
        return "Conversation history is empty."

    output = []

    for item in history:

        role = item["role"].capitalize()

        output.append(f"{role}: {item['content']}")

    return "\n".join(output)

def clear_memory():

    clear_history()

    return "Conversation memory cleared."

def question_count():

    history = get_history()

    count = sum(
        1
        for item in history
        if item["role"] == "user"
    )

    return f"You have asked {count} questions." 

def help_command():

    return """
==============================
      TITAN COMMANDS
==============================

help
    Show available commands

last question
    Display your previous question

show history
    Display conversation history

question count
    Count user questions

clear memory
    Clear conversation history

exit
    Exit Document Mode
"""       