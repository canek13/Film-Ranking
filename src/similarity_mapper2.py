#!/usr/bin/python3

"""
similarity_mapper2
"""

import sys
import pandas as pd
import numpy as np


big_data = pd.read_csv('ratings.csv')
all_films = np.unique(big_data.movieId)


for line in sys.stdin:
    film, film_statistics = line.strip().split('\t', 1)

    for f in all_films:
        if int(film) < f:
            print(film +','+ str(f) +'\t'+ film_statistics)
        else:
            print(str(f) +','+ film +'\t'+ film_statistics)
