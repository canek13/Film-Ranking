#!/usr/bin/python3

"""
rated_films_mapper1

For users' statistics file
It should be copied before this mapper for future tasks!
"""

import sys
import numpy as np

if __name__ == "__main__":
    for line in sys.stdin:

        user, films, ratings = line.strip().split('\t')

        ratings = ratings[1:-1].split(',')
        ratings = list(map(float,ratings))
        average = "{:.2f}".format(np.mean(ratings)) 
        #average = tofixed(sum(ratings) / len(ratings), 3)
        #average = sum(ratings) / len(ratings)

        films = films[1:-1].split(',')
        # the colision: first = '1', other = ' num'
        print(films[0] +'\t'+ user +'\t'+ str(ratings[0]) +'\t'+ average)

        for i,film in enumerate(films[1:], 1): # from second str
            print(film[1:] +'\t'+ user +'\t'+ str(ratings[i]) +'\t'+ average)
