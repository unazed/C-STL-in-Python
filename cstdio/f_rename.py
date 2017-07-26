"""
Rename a file entry
"""

import os  # would like to preferably not do this.


def rename(oldname, newname):
    os.rename(oldname, newname)
    
