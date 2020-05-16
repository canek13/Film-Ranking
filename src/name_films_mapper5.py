#!/usr/bin/python3

"""
name_films_mapper5
"""

import sys

for line in sys.stdin:
    if len(line.split(',')) >= 3: # film, it's name, gener
        if len(line.split(',')) == 3: 
            filmId, name, gener = line.strip().split(',')
            if name != 'title': # check if not header
                print(filmId +'\t0\t'+ name)
        elif line.find('"') != -1:
            #print(line)
            filmId, name, gener = line.strip().split('"')
            filmId = filmId[:-1] # film_name,
            print(filmId +'\t0\t'+ name) 
    else: # user, not_watched, rating
        #print(line.strip())
        key, rating = line.strip().split('\t')
        user, not_watched = key.split(',')
        print(user +'\t'+ not_watched +'\t'+ rating)
