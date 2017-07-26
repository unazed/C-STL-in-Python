"""
Returns a character from a given stream
"""

def getc(stream):
    with open(stream) as _stream:
        char = stream.read(1)
    return char

