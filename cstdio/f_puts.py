"""
Unformatted print to stdout
"""

def puts(arg):
    with open("/dev/stdout", 'w') as stdout:
        stdout.write("%s\n" % arg)

