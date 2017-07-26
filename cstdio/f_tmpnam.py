"""
Generates a name for a tempory file
"""

from random import randint  # would like to preferably not do this


def tmpnam():  # originally: char* str
    return "%s/%s%x.%x" % (chr(randint(97, 122)), chr(randint(97, 122)),
            randint(0, 255), randint(0, 255))

