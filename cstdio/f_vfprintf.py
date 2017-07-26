"""
Write formatted data from variable argument list to a file stream
"""

def vfprintf(stream, fmt, *args):
    stream.write(fmt % args)

