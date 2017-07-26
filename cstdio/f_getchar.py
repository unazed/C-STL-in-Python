"""
Returns character from stdin
"""

def getchar():
    with open("/dev/stdin") as stdin:
        char = stdin.read(1)
    return char

