"""
Read formatted data into variable argument list
"""

from f_vfscanf import vfscanf

def vscanf(fmt, *args):
    vfscanf(open("/dev/stdin"), fmt, args)

