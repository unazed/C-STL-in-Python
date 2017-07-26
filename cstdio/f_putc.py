"""
Write a character to a stream
"""

def putc(char, stream):
    with open(stream, 'w') as _stream:
        _stream.write(char)

