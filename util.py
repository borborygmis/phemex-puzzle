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

def to_hex(num):
    return hex(int(num)).lstrip("0x").rstrip("L")

def uncompressed_key(key):
    return Key(bytes_to_wif(key.to_bytes(), compressed=False))

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

def test_int(intk, addr='1h8BNZkhsPiu6EKazP19WkGxDw3jHf9aT'):
    try:
        priv_key_compressed = Key.from_int(int(intk))
        priv_key_uncompressed = uncompressed_key(priv_key_compressed)
    except:
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



