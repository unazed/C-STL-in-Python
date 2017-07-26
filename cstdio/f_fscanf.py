"""
Read formatted data from stream
"""

def fscanf(stream, fmt, argc):
    r_val = []
    for _ in range(argc):
        str_build = ""
        char = stream.read(1)
        if ord(char) == 0x0D or ord(char) == 0x0A:
            r_val.append(str_build)
            continue
        str_build += char
    return r_val

