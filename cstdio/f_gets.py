"""
Get string from stdin
"""

from f_fgets import fgets

def gets():  # originally: char* str
    return fgets(open('/dev/stdin'))

