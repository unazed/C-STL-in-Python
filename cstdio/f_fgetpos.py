"""
Get current position in stream
"""

def fgetpos(stream):  # originally: FILE* stream, fpos_t* pos
    return stream.tell()

