
def load_document(filename):
    with open(f"documents/{filename}", "r") as file:
        return file.read()