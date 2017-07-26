"""
Write formatted data to string
"""

def sprintf(fmt, *args):  # originally: char* str, const char* fmt, ...
    return fmt % args

