from chunker import create_chunks

text = """Requirement 1:
The system shall authenticate users.

Requirement 2:
The system shall encrypt passwords.

Requirement 3:
The system shall log failed login attempts.
"""

chunks = create_chunks(text)

for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}")
    print("-" * 30)
    print(chunk)