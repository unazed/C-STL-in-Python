"""
Write formatted data to a file stream
"""

def fprintf(stream, fmt, *args):
    stream.write(fmt % args)

