"""
Return position of cursor in file stream
"""

from f_fgetpos import fgetpos


def ftell(stream):
    return fgetpos(stream)
