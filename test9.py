"""
>>> adddec('XRP')
250
>>> adddec('Pheme')
495
>>> adddec('Phemex')
615
>>> 27 - slen(PRIME21E)
6
>>> muldec('XRP')
577280

Do concat of PRIME21E with two adddec or single muldec (as str).

Example:
    x = str(PRIME21E)+str(adddec('XRP'))+str(adddec('Phemex'))

Then different permutations of this.
"""

import time
from util import *

ES = str(PRIME21E)

def test1():
    print('- add -')
    # adddec test
    for p in product(WORDS, repeat=2):
        x1 = ES + str(adddec(p[0])) + str(adddec(p[1]))
        x2 = str(adddec(p[0])) + str(adddec(p[1])) + ES
        #print(p, len(x1), len(x2), ':',x1, ':', x2)
        test_int(x1)
        test_int(x2)

def test2():
    print('- add upper -')
    # adddec test
    for p in product(UWORDS, repeat=2):
        x1 = ES + str(adddec(p[0])) + str(adddec(p[1]))
        x2 = str(adddec(p[0])) + str(adddec(p[1])) + ES
        #print(p, len(x1), len(x2), ':',x1, ':', x2)
        test_int(x1)
        test_int(x2)

def test3():
    print('- add upper extra -')
    # adddec test
    for p in product(UWORDS_EXTRA, repeat=2):
        x1 = ES + str(adddec(p[0])) + str(adddec(p[1]))
        x2 = str(adddec(p[0])) + str(adddec(p[1])) + ES
        #print(p, len(x1), len(x2), ':',x1, ':', x2)
        test_int(x1)
        test_int(x2)

def test4():
    print('- mul -')
    # muldec test
    for p in WORDS:
        x1 = ES + str(muldec(p))
        x2 = str(muldec(p)) + ES
        #print(p, len(x1), len(x2), ':',x1, ':', x2)
        test_int(x1)
        test_int(x2)

def test5():
    print('- mul extra -')
    # muldec test
    for p in WORDS_EXTRA:
        x1 = ES + str(muldec(p))
        x2 = str(muldec(p)) + ES
        #print(p, len(x1), len(x2), ':',x1, ':', x2)
        test_int(x1)
        test_int(x2)

def test6():
    print('- mul upper extra -')
    # muldec test
    for p in UWORDS_EXTRA:
        x1 = ES + str(muldec(p))
        x2 = str(muldec(p)) + ES
        #print(p, len(x1), len(x2), ':',x1, ':', x2)
        test_int(x1)
        test_int(x2)

def test7():
    print('- mul upper -')
    # muldec test
    for p in UWORDS:
        x1 = ES + str(muldec(p))
        x2 = str(muldec(p)) + ES
        #print(p, len(x1), len(x2), ':',x1, ':', x2)
        test_int(x1)
        test_int(x2)

def test8():
    print('- add repeat=9 -')
    # make 3 digit ints 9 times
    for p in product(WORDS, repeat=9):
        x = ''
        for i in p:
            x += str(adddec(i))
        #print(p, len(x), ':',x)
        test_int(x)

def test9():
    print('- add repeat=9 upper -')
    # make 3 digit ints 9 times
    for p in product(UWORDS, repeat=9):
        x = ''
        for i in p:
            x += str(adddec(i))
        #print(p, len(x), ':',x)
        test_int(x)

def test10():
    print('- add repeat=9 extra -')
    # make 3 digit ints 9 times
    for p in product(WORDS_EXTRA, repeat=9):
        x = ''
        for i in p:
            x += str(adddec(i))
        #print(p, len(x), ':',x)
        test_int(x)

def test11():
    print('- add repeat=9 upper extra -')
    # make 3 digit ints 9 times
    for p in product(UWORDS_EXTRA, repeat=9):
        x = ''
        for i in p:
            x += str(adddec(i))
        #print(p, len(x), ':',x)
        test_int(x)

tests = [
    test1,
    test2,
    test3,
    test4,
    test5,
    test6,
    test7,
    #test8,
    test9,
    test10,
    test11,
]
for test in tests:
    test()
