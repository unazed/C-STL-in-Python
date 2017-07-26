"""
Read formatted data from stdin
"""

from f_fscanf import fscanf  # lazy

def scanf(fmt, *args):
    return fscanf(open('/dev/stdin'), fmt, args)

