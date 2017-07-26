"""
Seeks to a position in a file stream
"""

def fseek(stream, offset, origin):
    stream.seek(offset, origin)

