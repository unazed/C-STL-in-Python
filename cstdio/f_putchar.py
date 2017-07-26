"""
Writes a character to stdout.
Not to be confused with 'putc' which writes to an explicit stream
"""

def putchar(char):
    with open("/dev/stdout", 'w') as stdout:
        stdout.write(char)
