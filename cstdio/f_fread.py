"""
Read block of data from stream
"""

def fread(size, stream):  # originally: void* ptr, size_t size, size_t count, FILE* stream
    return stream.read(size)
