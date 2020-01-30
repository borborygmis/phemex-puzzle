# -*- coding: utf-8 -*-
"""
Tests converting words to integers in various ways using words from the puzzle's
picture.
"""

def testk0(words):
    sk = SigningKey.from_secret_exponent(PRIME21E, curve=SECP256k1)
    words = ''.join(words)
    n = ''
    for w in words:
        n += str(int(ord(w)))
    end = str(PRIME21E + int(n))
    print('{} {}:{} {}:{}'.format(words, len(n), n, len(end), end))
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
    print('{} {}:{} {}:{}'.format(words, len(n), n, len(end), end))
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
    print('{} {}:{} {}:{}'.format(words, len(n), n, len(end), end))
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
    print('{} {}:{} {}:{}'.format(words, len(n), n, len(end), end))
    test_int(n)
    test_int(end)

def testk4(words):
    words = ''.join(words)
    n = ''
    for w in words:
        n += str(int(ord(w)))
    end = str(PRIME21E + int(n))
    print('{} {}:{} {}:{}'.format(words, len(n), n, len(end), end))
    test_int(n)
    test_int(end)

def testk5(words):
    words = ''.join(words)
    n = 0
    for w in words:
        n += int(ord(w))
    n = str(n)
    end = str(PRIME21E + int(n))
    print('{} {}:{} {}:{}'.format(words, len(n), n, len(end), end))
    test_int(n)
    test_int(end)

def testk6(words):
    words = ''.join(words)
    n = []
    for w in words:
        n.append(str(int(ord(w))*PRIME21E))
    n = ''.join(n)
    end = str(PRIME21E + int(n))
    print('{} {}:{} {}:{}'.format(words, len(n), n, len(end), end))
    test_int(n)
    test_int(end)

def testk7(words):
    words = ''.join(words)
    n = []
    for w in words:
        n.append(str(int(ord(w))*PRIME21E))
    n = ''.join(sorted(n))
    end = str(PRIME21E + int(n))
    print('{} {}:{} {}:{}'.format(words, len(n), n, len(end), end))
    test_int(n)
    test_int(end)

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
    coins = ['XRP', 'BTC', 'ETH',] # 'Phemex']
    for coin in coins:
        test_all([coin, 'Phemex'])
        test_all(['Phemex', coin])

    for p in permutations(coins):
        test_all(p)

    coins_extra = coins + 'First 21-digit prime found in consecutive digits of e'.split(' ')
    coins_extra = coins_extra + ['Phemex',]
    for p in permutations(coins_extra, 3):
        test_all(p)
    for p in permutations(coins_extra, 2):
        test_all(p)

if __name__ == '__main__':
    main()
