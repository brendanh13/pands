# More Prep for Problem Sheet 7

import sys

with open(sys.argv[1], 'r') as f:
    contents = f.read()

def letterFrequency(f, letter):
    return contents.count(letter)

print(letterFrequency(f, 'e'))    