# -*- coding: utf-8 -*-
"""
Tests converting words to integers in various ways using words from the puzzle's
picture.
"""
from util import *

def dprint(s):
    return #print(s)

def testk0(words):
    sk = SigningKey.from_secret_exponent(PRIME21E, curve=SECP256k1)
    words = ''.join(words)
    n = ''
    for w in words:
        n += str(int(ord(w)))
    end = str(PRIME21E + int(n))
    dprint('{} {}:{} {}:{}'.format(words, len(n), n, len(end), end))
    sig = sk.sign(n.encode())
    test_hex(sig.hex())
    sig = sk.sign(end.encode())
    test_hex(sig.hex())
    h = hashlib.sha256(end.encode()).hexdigest()
    sig = sk.sign(h.encode())
    test_hex(sig.hex())
    h = hashlib.sha256(n.encode()).hexdigest()
    sig = sk.sign(h.encode())
    test_hex(sig.hex())

def testk1(words):
    words = ''.join(words)
    n = ''
    for w in words:
        n += str(int(ord(w)))
    end = str(PRIME21E + int(n))
    dprint('{} {}:{} {}:{}'.format(words, len(n), n, len(end), end))
    test_hex(to_hex(n))
    test_hex(to_hex(end))

def testk2(words):
    sk = SigningKey.from_secret_exponent(PRIME21E, curve=SECP256k1)
    words = ''.join(words)
    n = []
    for w in words:
        n.append(str(int(ord(w))))

    n = ''.join(sorted(n))
    end = str(PRIME21E + int(n))
    dprint('{} {}:{} {}:{}'.format(words, len(n), n, len(end), end))
    sig = sk.sign(n.encode())
    test_hex(sig.hex())
    h = hashlib.sha256(end.encode()).hexdigest()
    sig = sk.sign(h.encode())
    test_hex(sig.hex())

def testk3(words):
    words = ''.join(words)
    n = []
    for w in words:
        n.append(str(int(ord(w))))
    n = ''.join(sorted(n))
    end = str(PRIME21E + int(n))
    dprint('{} {}:{} {}:{}'.format(words, len(n), n, len(end), end))
    test_int(n, do_endian=True)
    test_int(end, do_endian=True)

def testk4(words):
    words = ''.join(words)
    n = ''
    for w in words:
        n += str(int(ord(w)))
    end = str(PRIME21E + int(n))
    dprint('{} {}:{} {}:{}'.format(words, len(n), n, len(end), end))
    test_int(n, do_endian=True)
    test_int(end, do_endian=True)

def testk5(words):
    words = ''.join(words)
    n = 0
    for w in words:
        n += int(ord(w))
    n = str(n)
    end = str(PRIME21E + int(n))
    dprint('{} {}:{} {}:{}'.format(words, len(n), n, len(end), end))
    test_int(n, do_endian=True)
    test_int(end, do_endian=True)

def testk6(words):
    words = ''.join(words)
    n = []
    for w in words:
        n.append(str(int(ord(w))*PRIME21E))
    n = ''.join(n)
    end = str(PRIME21E + int(n))
    dprint('{} {}:{} {}:{}'.format(words, len(n), n, len(end), end))
    test_int(n, do_endian=True)
    test_int(end, do_endian=True)

def testk7(words):
    words = ''.join(words)
    n = []
    for w in words:
        n.append(str(int(ord(w))*PRIME21E))
    n = ''.join(sorted(n))
    end = str(PRIME21E + int(n))
    dprint('{} {}:{} {}:{}'.format(words, len(n), n, len(end), end))
    test_int(n, do_endian=True)
    test_int(end, do_endian=True)

def test_all(li):
    tests = (
        testk0,
        testk1,
        testk2,
        testk3,
        testk4,
        testk5,
        testk6,
        testk7,
    )
    for test in tests:
        test(li)

def main():
    print('t:1')
    for p in permutations(WORDS):
        print(p)
        test_all(p)
    print('t:2')
    for p in permutations(WORDS, 3):
        test_all(p)
    print('t:3')
    for p in permutations(WORDS, 2):
        test_all(p)
    #for p in permutations(WORDS_EXTRA, 4):
    #    test_all(p)
    print('t:4')
    for p in permutations(WORDS_EXTRA, 3):
        test_all(p)
    print('t:5')
    for p in permutations(WORDS_EXTRA, 2):
        test_all(p)

if __name__ == '__main__':
    main()
