# -*- coding: utf-8 -*-
"""
Tests converting words to integers in various ways using words from the puzzle's
picture.
"""
from util import *
from bit.utils import hex_to_int
from bit.utils import flip_hex_byte_order

def flipint(i):
    return hex_to_int(flip_hex_byte_order(to_hex(i)))

def flipstr(s):
    return hex_to_int(flip_hex_byte_order(tohex(s)))

PRIME21E_REV = flipint(PRIME21E)

def test(x):
    if slen(x) != 27:
        return
    print(x, slen(x))
    for pe in (PRIME21E_REV, PRIME21E):
        test_int(x*pe, debug=False)
        test_int(x+pe, debug=False)
        test_int(x-pe, debug=False)
        test_int(x//pe, debug=False)
        test_int(x|pe, debug=False)
        test_int(pe|x, debug=False)
        test_int(x^pe, debug=False)
        test_int(pe^x, debug=False)
        test_int(x%pe, debug=False)
        test_int(pe%x, debug=False)
        test_int(modular_sqrt(x, pe))
    test_int(x, debug=False)

def maybe(s):
    x = flipstr(s)
    test(x)

def main():
    for p in permutations(WORDS_EXTRA, 3):
        maybe(''.join(p))

if __name__ == '__main__':
    main()

