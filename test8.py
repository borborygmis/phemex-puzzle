from util import *

data = open('satoshipuzzle.png', 'rb').read()
pos = 0
ld = len(data)
pi = 0
while pos < len(data)-16:
    part = utils.bytes_to_hex(data[pos:pos+16])
    for i in range(22, len(part)):
        n = int(part[:i], 16)
        if slen(n) == 27:
            pi += 1
            if pi % 1000 == 0:
                print(slen(n), n, '%.2f' % (pos/ld*100))
            test_int(n)
            test_int(n+PRIME21E)
            test_int(n*PRIME21E)
            test_int(n-PRIME21E)
    pos += 1



