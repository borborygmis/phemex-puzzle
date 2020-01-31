# -*- coding: utf-8 -*-
"""
reused functions, constants, imports, etc
"""
from math import e
import hashlib
from itertools import permutations

from bit import Key
from bit.format import bytes_to_wif
from ecdsa import SigningKey, SECP256k1

PRIME21E = 957496696762772407663
TARGET_LEN = 27
COMPRESSED_PUBLIC_KEY = '02b4a72e4aaa69ba04b80c6891df01f50d191a65eccc61e4e9862d1e421ce815b3'
PUBLIC_ADDRESS = '1h8BNZkhsPiu6EKazP19WkGxDw3jHf9aT'
#WORDS = ['XRP', 'BTC', 'ETH', 'Phemex']
#WORDS = ['957496696762772407663', 'XRP', 'BTC', 'ETH', 'Phemex']
WORDS = ['957496696762772407663', 'XRP', 'BTC', 'ETH', 'Phemex', 'Pheme', 'Mex']
WORDS_EXTRA = WORDS + 'First 21-digit prime found in consecutive digits of e'.split(' ')

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

def tohn(s):
    return int(tohex(s), 16)

def slen(n):
    return len(str(n))

def test_key(key, addr):
    if (str(key.address) == str(addr)):
        print('-*-'*30)
        print('-*-'*30)
        print('found private key!')
        print(key.to_wif())
        print('-*-'*30)
        print('-*-'*30)
        print(key.get_balance('btc'))
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

def test_int(intk, addr='1h8BNZkhsPiu6EKazP19WkGxDw3jHf9aT'):
    try:
        priv_key_compressed = Key.from_int(int(intk))
        priv_key_uncompressed = uncompressed_key(priv_key_compressed)
    except Exception as err:
        print("ERROR: test_int:", err)
        return False
    """Debug:
    print('addrc:{} addru:{} wifc:{} wifu:{}'.format(
        priv_key_compressed.address,
        priv_key_uncompressed.address,
        priv_key_compressed.to_wif(),
        priv_key_uncompressed.to_wif(),

    ))
    """
    if test_key(priv_key_compressed, addr):
        return True
    if test_key(priv_key_uncompressed, addr):
        return True
    return False

def test_hex(hex, addr='1h8BNZkhsPiu6EKazP19WkGxDw3jHf9aT'):
    if (len(hex) > 64):
        return False
    priv_key_compressed = Key.from_hex(hex)
    priv_key_uncompressed = uncompressed_key(priv_key_compressed)
    if test_key(priv_key_compressed, addr):
        return True
    if test_key(priv_key_uncompressed, addr):
        return True
    return False



