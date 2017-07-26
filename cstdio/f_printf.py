"""
Print formatted data to stdout.
"""


def printf(fmt, *arg):
    with open("/dev/stdout", 'w') as stdout:
        stdout.write(fmt % arg)

