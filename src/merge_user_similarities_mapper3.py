#!/usr/bin/python3

"""
merge_user_similarities_mapper3
"""

import sys
import numpy as np
import pandas as pd

big_data = pd.read_csv('ratings.csv', sep=',', header=None)
all_films = np.unique(big_data[1])
big_data = 0

for line in sys.stdin:
    key, value = line.strip().split('\t',1)

    if len(key.split(',')) == 2: #similarity
        print(key +',0\t'+ value)
    else: # user with statisctics
        watched, ratings = value.split('\t')
        watched = list(map(int, watched[1:-1].split(',')))
        ratings = list(map(float, ratings[1:-1].split(',')))
        not_watched = np.setdiff1d(all_films, watched, assume_unique=True)
        for not_w in not_watched:
            for i,w in enumerate(watched):
                if not_w < w:
                    if (not_w, w) in existed_sim:
                    #if np.intersect1d(np.where(f1 == not_w)[0], np.where(f2 == w)[0], assume_unique=True).size > 0:
                        print(str(not_w) +','+ str(w) +','+ key +',1\t'+ str(ratings[i]))
                else:
                    if (w, not_w) in existed_sim:
                    #if np.intersect1d(np.where(f1 == w)[0], np.where(f2 == not_w)[0], assume_unique=True).size > 0:
                        print(str(w) +','+ str(not_w) +','+ key +',2\t'+ str(ratings[i]))

