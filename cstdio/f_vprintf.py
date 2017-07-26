"""
Print formatted data from variable argument list to stdout
"""

from f_vfprintf import vfprintf

def vprintf(fmt, *args):
    vfprintf(open('/dev/stdout', 'w'), fmt, args)

