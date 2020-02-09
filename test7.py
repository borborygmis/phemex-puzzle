import time
from util import *

def concat(wints, size):
    print('-{}-'.format(size))
    time.sleep(1)
    for p in permutations(wints, size):
        x = ''
        for i in p:
            x += str(i)
        if len(x) == 27:
            for pp in permutations(p):
                y = ''
                for i in pp:
                    y += str(i)
                print('con:', size, '27:', y)
                test_int(y)
                test_int(int(y)+PRIME21E)
                test_int(int(y)*PRIME21E)
                test_int(int(y)-PRIME21E)

def multiply(wints, size):
    print('-{}-'.format(size))
    time.sleep(1)
    for p in permutations(wints, size):
        x = 1
        for pp in p:
            x *= pp
        if slen(x) == 27:
            print('mul:', size, '27:', x, p)
            test_int(x)
            test_int(int(x)+PRIME21E)
            test_int(int(x)*PRIME21E)
            test_int(int(x)-PRIME21E)
            break # stop since they'll all equal the same

def addition(wints, size):
    print('-{}-'.format(size))
    time.sleep(1)
    for p in permutations(wints, size):
        x = 0
        for pp in p:
            x += pp
        if slen(x) == 27:
            print('add:', size, '27:', x, p)
            test_int(x)
            test_int(int(x)+PRIME21E)
            test_int(int(x)*PRIME21E)
            test_int(int(x)-PRIME21E)
            break # stop since they'll all equal the same

wints = []
for w in WORDS_EXTRA:
    wints.append(int(tohex(w), 16))

"""
for i in range(1, 6):
    concat(wints, i)
"""
for i in range(2, len(wints)):
    addition(wints, i)

for i in range(2, 8):
    multiply(wints, i)

