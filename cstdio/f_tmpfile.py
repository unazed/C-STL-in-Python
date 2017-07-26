"""
Open a temporary file
"""

from f_tmpnam import tmpnam


def tmpfile():
    return open(tmpnam(), 'w+b')

