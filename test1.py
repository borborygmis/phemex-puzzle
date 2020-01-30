# -*- coding: utf-8 -*-
"""
Tests converting words to integers in various ways using words from the puzzle's
picture.
"""
from util import *

def tohex(s):
    o = ''
    for c in s:
        x = str( hex(ord(c) ))[2:]
        o += x
    return o

def tohn(s):
    return int(tohex(s), 16)

def slen(n):
    return len(str(n))

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
    coins = ['XRP', 'BTC', 'ETH', 'Phemex']
    for p in permutations(coins):
        maybe(''.join(p))

    for p in permutations(coins, 3):
        maybe(''.join(p))
    
    for p in permutations(coins, 2):
        maybe(''.join(p))

    coins_extra = coins + 'First 21-digit prime found in consecutive digits of e'.split(' ')
    for p in permutations(coins_extra, 5):
        maybe(''.join(p))
    for p in permutations(coins_extra, 4):
        maybe(''.join(p))
    for p in permutations(coins_extra, 3):
        maybe(''.join(p))
    for p in permutations(coins_extra, 2):
        maybe(''.join(p))

if __name__ == '__main__':
    main()

