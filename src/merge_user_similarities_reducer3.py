#!/usr/bin/python3

"""
merge_user_similarities_reducer3
"""

import sys

i = -1
j = -1

for line in sys.stdin:
    key, value = line.strip().split('\t')
    if len(key.split(',')) == 3: # similarity
        i, j,_ = list(map(int, key.split(',')))
        sim = value
    else: # user's films to check fo similarity
        w1, w2, u, key_not_w = list(map(int, key.split(',')))
        if w1 == i and w2 == j:
            if float(value): # rating_w != 0
                if key_not_w == 1:
                    print(str(u) +','+ str(w1) +'\t'+ sim +'\t'+ value)
                else:
                    print(str(u) +','+ str(w2) +'\t'+ sim +'\t'+ value)
