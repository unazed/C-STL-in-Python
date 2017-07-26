"""
Read formatted data from stream into variable argument list
"""

def vfscanf(stream, fmt, *args):
    return fmt % stream.read()  # is this correct?

