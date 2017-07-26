"""
Return string from stream
"""

def fgets(stream):
    str_build = ""
    while 1:
        char = stream.read(1)
        if ord(char) == 0x0A or ord(char) == 0x0D:
            break
        str_build += char
    return str_build

