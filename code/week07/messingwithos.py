# Messing with OS Module

# Author: Brendan Heeney

import os

filename = 'test.txt'
if os.path.exists(filename):
    print(filename, "already exists")
    os.remove(filename)
else:
    print(filename, "does not exist")