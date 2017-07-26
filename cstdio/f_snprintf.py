"""
Write formatted output to sized buffer
"""

def snprintf(strlength, fmt, *args):  # originally: char* s, size_t n, const char* fmt, ...
    return (fmt % args)[:strlength-1]

