# -*- coding: utf-8 -*-
"""
Tests converting words to integers in various ways using words from the puzzle's
picture.
"""
from util import *
from bit.utils import hex_to_int

def test(x):
    if slen(x) != 27:
        return
    print(x, slen(x), modular_sqrt(x, PRIME21E), modular_sqrt(PRIME21E, x))
    test_int(modular_sqrt(x, PRIME21E))
    test_int(modular_sqrt(PRIME21E, x))
    test_int(x, debug=False)

def maybe(s):
    x = hex_to_int(tohex(s))
    test(x)

def main():
    for p in permutations(WORDS, 5):
        maybe(''.join(p))
    for p in permutations(WORDS, 4):
        maybe(''.join(p))
    for p in permutations(WORDS, 3):
        maybe(''.join(p))
    for p in permutations(WORDS, 2):
        maybe(''.join(p))

if __name__ == '__main__':
    main()

