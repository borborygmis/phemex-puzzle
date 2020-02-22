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

# adddec test
for p in product(WORDS, repeat=2):
    x1 = ES + str(adddec(p[0])) + str(adddec(p[1]))
    x2 = str(adddec(p[0])) + str(adddec(p[1])) + ES
    #print(p, len(x1), len(x2), ':',x1, ':', x2)
    test_int(x1)
    test_int(x2)

# adddec test
for p in product(UWORDS, repeat=2):
    x1 = ES + str(adddec(p[0])) + str(adddec(p[1]))
    x2 = str(adddec(p[0])) + str(adddec(p[1])) + ES
    #print(p, len(x1), len(x2), ':',x1, ':', x2)
    test_int(x1)
    test_int(x2)


# muldec test
for p in WORDS:
    x1 = ES + str(muldec(p))
    x2 = str(muldec(p)) + ES
    #print(p, len(x1), len(x2), ':',x1, ':', x2)
    test_int(x1)
    test_int(x2)

# muldec test
for p in UWORDS:
    x1 = ES + str(muldec(p))
    x2 = str(muldec(p)) + ES
    #print(p, len(x1), len(x2), ':',x1, ':', x2)
    test_int(x1)
    test_int(x2)

# make 3 digit ints 9 times
for p in product(WORDS, repeat=9):
    x = ''
    for i in p:
        x += str(adddec(i))
    #print(p, len(x), ':',x)
    test_int(x)

# make 3 digit ints 9 times
for p in product(UWORDS, repeat=9):
    x = ''
    for i in p:
        x += str(adddec(i))
    #print(p, len(x), ':',x)
    test_int(x)
