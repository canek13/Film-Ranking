#!/usr/bin/python3

"""
similarity_reducer2
"""

import sys
import numpy as np

def similarity(i_ind, j_ind, r_i, r_j, a):
    r_i = np.array(list(map(float, r_i[1:-1].split(','))))[i_ind]
    r_j = np.array(list(map(float, r_j[1:-1].split(','))))[j_ind]
    a = np.array(list(map(float, a[1:-1].split(','))))[i_ind]
    
    if np.dot(r_i - a, r_j - a) == 0:
        return 0
    sim = np.dot(r_i - a, r_j - a) / \
        (np.linalg.norm(r_i - a) * np.linalg.norm(r_j - a))
    if sim < 0:
        return 0
    else:
        return sim

previous_key = None
previous_statistics = None

for line in sys.stdin:
    key, statistics = line.strip().split('\t',1)
    if key != previous_key:
        previous_key = key
        previous_statistics = statistics
    else:
        users_j, ranks_j, averages_j = statistics.strip().split('\t')
        users_i, ranks_i, averages_i = previous_statistics.strip().split('\t')
        users_i = list(map(int,users_i[1:-1].split(',')))
        users_j = list(map(int,users_j[1:-1].split(',')))
        inters, i_ind, j_ind = np.intersect1d(users_i, users_j, 
                assume_unique=True, return_indices=True)
        if inters.size:
            sim = "{:.2f}".format(similarity(i_ind, j_ind, ranks_i, ranks_j, averages_i))
            print(key +'\t'+ sim)
