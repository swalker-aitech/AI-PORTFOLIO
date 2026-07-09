# Load document once
def load_document():
    with open("documents/sample.txt", "r") as file:
        return file.read()