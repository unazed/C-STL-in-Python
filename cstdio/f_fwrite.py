"""
Write block of data to stream
"""

def fwrite(data, stream):  # originally: void* ptr, size_t size, size_t count, FILE* stream
    stream.write(data)

