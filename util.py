# -*- coding: utf-8 -*-
"""
reused functions, constants, imports, etc
"""
import sys
import traceback
from math import e
import hashlib
from itertools import permutations, product
import struct

from bit import Key
from bit.format import bytes_to_wif
from bit.utils import bytes_to_hex
from bit.base58 import b58encode, b58decode
import bit.utils as utils
from ecdsa import SigningKey, SECP256k1

PRIME21E = 957496696762772407663
TARGET_LEN = 27
COMPRESSED_PUBLIC_KEY = '02b4a72e4aaa69ba04b80c6891df01f50d191a65eccc61e4e9862d1e421ce815b3'
COMP_PUBLIC_ADDRESS = '1h8BNZkhsPiu6EKazP19WkGxDw3jHf9aT'
UNCP_PUBLIC_ADDRESS = '1LPmwxe59KD6oEJGYinx7Li1oCSRPCSNDY'

#WORDS = ['XRP', 'BTC', 'ETH', 'Phemex']
#WORDS = ['957496696762772407663', 'XRP', 'BTC', 'ETH', 'Phemex']
#WORDS = ['XRP', 'BTC', 'ETH', 'Phemex', 'Pheme',]
#WORDS = ['957496696762772407663', 'XRP', 'BTC', 'ETH', 'Phemex', 'Pheme', 'Mex', 'mex']
# lower
WORDS = ['XRP', 'BTC', 'ETH', 'Phemex', 'Pheme', 'Satoshi', 'Nakamoto'] #, "Φήμη" #'957496696762772407663']
WORDS_EXTRA = WORDS + 'First 21-digit prime found in consecutive digits of e'.split(' ')
# reversed
RWORDS = [i[::-1] for i in WORDS]
RWORDS_EXTRA = [i[::-1] for i in WORDS_EXTRA]
#upper
UWORDS = [i.upper() for i in WORDS]
UWORDS_EXTRA = [i.upper() for i in WORDS_EXTRA]

def ordstr(s):
    x = ''
    for i in s:
        x += str(ord(i))
    return x

def right_pad_zed(cur):
    return cur+(64-len(cur))*'0'

def to_binary(s):
    return ''.join(format(i, 'b') for i in bytearray(s, encoding='utf-8'))

def to_hex(num):
    return hex(int(num)).lstrip("0x").rstrip("L")

def tohex(s):
    o = ''
    for c in s:
        x = str( hex(ord(c) ))[2:]
        o += x
    return o

def uncompressed_key(key):
    return Key(bytes_to_wif(key.to_bytes(), compressed=False))

def compressed_key(key):
    return Key(bytes_to_wif(key.to_bytes(), compressed=True))

def adddec(s):
    t = 0
    for i in s:
        t += ord(i)
    return t

def muldec(s):
    t = 1
    for i in s:
        t *= ord(i)
    return t

def tohn(s):
    return int(tohex(s), 16)

def slen(n):
    return len(str(n))

def test_key(key):
    found = False
    if str(key.address) == COMP_PUBLIC_ADDRESS or \
            str(key.address) == UNCP_PUBLIC_ADDRESS:
        found = True
    if key.pub_to_hex() == COMPRESSED_PUBLIC_KEY:
        found = True
    if found:
        print('-*-'*30)
        print('-*-'*30)
        print('found private key!')
        print(key.to_wif())
        print('-*-'*30)
        print('-*-'*30)
        print(key.get_balance())
        print('-*-'*30)
        print('-*-'*30)
        exit(0) #kill it since we found the key
        return True
    return False

def key_from_int_comp(intk):
    return Key.from_int(int(intk))

def key_from_int_uncomp(intk):
    priv_key_compressed = Key.from_int(int(intk))
    priv_key_uncompressed = uncompressed_key(priv_key_compressed)
    return priv_key_uncompressed

def key_from_hex_comp(intk):
    return Key.from_hex(intk)

def key_from_hex_uncomp(intk):
    priv_key_compressed = Key.from_hex(intk)
    priv_key_uncompressed = uncompressed_key(priv_key_compressed)
    return priv_key_uncompressed

def test_int(intk, debug=False, do_endian=True, do_ops=True):
    if do_ops:
        test_with_prime21e_ops(intk)
    if do_endian:
        n = int(intk)
        n2 = int.from_bytes(n.to_bytes((n.bit_length() + 7) // 8, 'big') or b'\0', byteorder='little')
        #print(n, '->', n2)
        test_int(n2, do_endian=False, do_ops=False)
        # concat PRIME21E
        n3 = str(intk)+str(PRIME21E)
        n4 = str(PRIME21E)+str(intk)
        test_int(n3, do_endian=False, do_ops=False)
        test_int(n4, do_endian=False, do_ops=False)
        #test_int(struct.pack('>L', int(intk)))

    if int(intk) == 0 or int(intk) > 115792089237316195423570985008687907852837564279074904382605163141518161494337:
        return 'invalid size'
    try:
        sha_hex = to_hex(intk)
        sha_key = right_pad_zed(sha_hex)
        #print(len(sha_key), sha_hex, '->', sha_key)
        sha_key_compressed = Key.from_hex(sha_key)
        sha_key_uncompressed = uncompressed_key(sha_key_compressed)
        priv_key_compressed = Key.from_int(int(intk))
        priv_key_uncompressed = uncompressed_key(priv_key_compressed)
        #priv_key_compressed2 = compressed_key(int(intk))
        priv_key_compressed2 = compressed_key(priv_key_compressed) #int(intk))
        priv_key_compressed3 = Key.from_int(int(intk)&PRIME21E)
        priv_key_c2 = Key.from_bytes(
            b58decode(b58encode(
                utils.hex_to_bytes(utils.int_to_hex(int(intk)))
            ))
        )
        priv_key_uc2 = uncompressed_key(priv_key_c2)
    except Exception as err:
        print("ERROR: test_int:", err, 'intk:', intk)
        traceback.print_exc(file=sys.stdout)
        return False
    """Debug:
    print('addrc:{} addru:{} wifc:{} wifu:{}'.format(
        priv_key_compressed.address,
        priv_key_uncompressed.address,
        priv_key_compressed.to_wif(),
        priv_key_uncompressed.to_wif(),

    ))
    """
    if debug:
        print(
            intk,
            priv_key_compressed.address,
            priv_key_uncompressed.address,
            bytes_to_hex(priv_key_compressed.public_key),
            bytes_to_hex(priv_key_uncompressed.public_key),
        )
    if test_key(sha_key_compressed):
        return True
    if test_key(sha_key_uncompressed):
        return True
    if test_key(priv_key_compressed3):
        return True
    if test_key(priv_key_compressed):
        return True
    if test_key(priv_key_compressed2):
        return True
    if test_key(priv_key_uncompressed):
        return True
    if test_key(priv_key_uc2):
        return True
    if test_key(priv_key_c2):
        return True
    return False

def test_hex(hex):
    if (len(hex) > 64):
        return False
    priv_key_compressed = Key.from_hex(hex)
    priv_key_uncompressed = uncompressed_key(priv_key_compressed)
    if test_key(priv_key_compressed):
        return True
    if test_key(priv_key_uncompressed):
        return True
    return False

def test_with_prime21e_ops(i):
    """Try test_int a bunch of ways using the prime from e"""
    i2 = int(str(i)+str(i))
    for x in (i, i2):
        x = int(x)
        test_int(x, do_ops=False)
        test_int(x*2, do_ops=False)
        test_int(x+PRIME21E, do_ops=False)
        test_int(x*PRIME21E, do_ops=False)
        test_int(x//PRIME21E, do_ops=False)
        test_int(x|PRIME21E, do_ops=False)
        test_int(x^PRIME21E, do_ops=False)
        test_int(x%PRIME21E, do_ops=False)

def modular_sqrt(a, p):
    def legendre_symbol(a, p):
        ls = pow(a, (p - 1) // 2, p)
        return -1 if ls == p - 1 else ls
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)
    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1
    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m

    #print(modular_sqrt(223, 17)) # should return 6
