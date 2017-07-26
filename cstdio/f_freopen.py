"""
Reopen a file stream with different settings
"""

def freopen(filename, mode, stream):  # stream argument not used
    return open(filename, mode)

