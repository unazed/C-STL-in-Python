"""
Sets the position of the cursor in a file stream
"""

from f_fseek import fseek


def fsetpos(stream, pos):
    fseek(stream, pos, 0)

