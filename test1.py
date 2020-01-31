# -*- coding: utf-8 -*-
"""
Tests converting words to integers in various ways using words from the puzzle's
picture.
"""
from util import *

def maybe0(s):
    n = tohn(s)
    if slen(n) == 27:
        print(s, tohex(s), n, slen(n))
        test_hex(tohex(s))
        test_hex(to_hex(n))
        test_int(n)

def maybe1(s):
    n = tohn(s) * PRIME21E
    if slen(n) == 27:
        print(s, tohex(s), n, slen(n))
        test_hex(to_hex(n))
        test_int(n)

def maybe(s):
    maybe0(s)
    maybe1(s)

def main():
    for p in permutations(WORDS):
        maybe(''.join(p))
    for p in permutations(WORDS, 4):
        maybe(''.join(p))
    for p in permutations(WORDS, 3):
        maybe(''.join(p))
    for p in permutations(WORDS, 2):
        maybe(''.join(p))
    for p in permutations(WORDS_EXTRA, 5):
        maybe(''.join(p))
    for p in permutations(WORDS_EXTRA, 4):
        maybe(''.join(p))
    for p in permutations(WORDS_EXTRA, 3):
        maybe(''.join(p))
    for p in permutations(WORDS_EXTRA, 2):
        maybe(''.join(p))

if __name__ == '__main__':
    main()

