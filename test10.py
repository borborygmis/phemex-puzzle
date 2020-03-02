"""
Interesting... "consecutive" converts to a 27 digit integer and kind of lines
up with Pheme repeating what she learns (twice within 3 days)... maybe?
"""

from util import *
from bit.crypto import sha256, double_sha256

word = 'consecutive'
print('word:{} hex:{} len:{} int:{}'.format(word, word.encode().hex(), len(str(int(word.encode().hex(), 16))), int(word.encode().hex(), 16)))

word_int = int(word.encode().hex(), 16)

for length in (11, 12, 16):
    test_key( Key.from_bytes(double_sha256(word_int.to_bytes(length=length, byteorder='big'))) )
    test_key( Key.from_bytes(double_sha256(word_int.to_bytes(length=length, byteorder='little'))) )
    test_key( Key.from_bytes(sha256(word_int.to_bytes(length=length, byteorder='big'))) )
    test_key( Key.from_bytes(sha256(word_int.to_bytes(length=length, byteorder='little'))) )

print('Done. Nothing found.')
