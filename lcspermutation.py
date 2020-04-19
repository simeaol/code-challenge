#!/bin/python3

import os
import sys

#
# Complete the tutzkiAndLcs function below.
#
def tutzkiAndLcs(a, b):
    seq = [0]*10
    print('{0} and {1}'.format(a, b))
    m = lcs(seq, a, b, len(a)-1, len(b)-1)#lcs between a and b before interpolation
    print(seq)
    print("lcs before interpolation= {0}".format(m))

    per = permutation(a, b, len(a)-1, len(b)-1)
    print('lcs after permutation={0}'.format(per))

    return m
def permutation(a, b, p1, p2):
    
    total = 0
    maps = {}
    for i in range(0, len(b)):
        seq = [0]*10
        new = b[i] + a
        maps[new]=False
        print(maps)
        if(maps.keys > 1):
            break
        print(new)
        total += lcs(seq,  new, b, len(new)-1, len(b)-1)
        print(seq)
    return total

def lcs(seq, a, b, p1, p2):
    if p1 < 0 or p2 < 0:
        return 0;
    elif a[p1]==b[p2]:
        seq[p1] = a[p1]
        return lcs(seq, a, b, p1-1, p2-1) + 1
    else:
        return max(lcs(seq, a, b, p1-1, p2), lcs(seq, a, b, p1, p2-1))


if __name__ == '__main__':

    a = 'aa'

    b = 'baaa'

    result = tutzkiAndLcs(a, b)
    print('result={0}'.format(result))
