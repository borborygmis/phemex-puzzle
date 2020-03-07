"""
Interesting... "consecutive" converts to a 27 digit integer and kind of lines
up with Pheme repeating what she learns (twice within 3 days)... maybe?
"""

from util import *
from bit.crypto import sha256, double_sha256

def maybe(i, length):
    try:
        test_key( Key.from_bytes(double_sha256(i.to_bytes(length=length, byteorder='big'))) )
        test_key( Key.from_bytes(double_sha256(i.to_bytes(length=length, byteorder='little'))) )
        test_key( Key.from_bytes(sha256(i.to_bytes(length=length, byteorder='big'))) )
        test_key( Key.from_bytes(sha256(i.to_bytes(length=length, byteorder='little'))) )
    except Exception as err:
        print('ERROR: i={} length={}'.format(i, length))
        pass

def main():
    word = 'consecutive'
    word_int = int(word.encode().hex(), 16)
    word_int2 = int(str(word_int)*2)
    zero_padded1 = '000000000000000000000000000000000000000000000000000000000000000000000000000000'
    zero_padded2 = '000000000000000000000000000000000000000000000000000000000000000000000000000000'
    zero_padded1 = str(word_int) + '0'*(len(zero_padded1)-len(str(word_int)))
    zero_padded2 = str(word_int2) + '0'*(len(zero_padded2)-len(str(word_int2)))
    test_with_prime21e_ops(zero_padded1)
    test_with_prime21e_ops(zero_padded2)
    test_with_prime21e_ops(word_int)
    test_with_prime21e_ops(word_int2)
    print('word:{} hex:{} len:{} int:{}'.format(
        word,
        word.encode().hex(),
        len(str(int(word.encode().hex(), 16))),
        word_int)
    )
    print('zpad:', zero_padded1, zero_padded2)

    for length in range(11, 33):
        maybe(word_int, length)
        maybe(word_int2, length)

    print('Done. Nothing found.')

if __name__ == '__main__':
    main()
