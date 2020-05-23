#!/usr/bin/python3

"""
name_films_reducer5
"""

import sys

name = ''

for line in sys.stdin:
    filmId, user, rating = line.strip().split('\t')
    if user == '0': # rating = name of film
        name = rating
    else:
        print(user +'\t'+ name +'\t'+ rating)
