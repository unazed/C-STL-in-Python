"""
Changes the buffer mode of a file stream
"""

def setbuf(stream, _buffer):  # _buffer is 0/1 only.
    _stream = open(stream.name, stream.mode, _buffer)
    stream.close()
    return _stream
