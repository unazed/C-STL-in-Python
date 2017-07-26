"""
Unget a character from a file stream
"""

def ungetc(char, stream):
    stream.seek(stream.tell()-1)
    stream.write(char)
    stream.seek(stream.tell()-1)

