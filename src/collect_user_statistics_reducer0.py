#!/usr/bin/python3
import numpy
import sys

previous_user = None
watched_rating = []
watched = []

for line in sys.stdin:
    user, movie, rating = line.strip().split('\t')

    if user != previous_user:
        if previous_user: # check if not None
            print(previous_user +'\t'+ str(watched) +'\t'+ str(watched_rating))
        watched = [int(movie)]
        watched_rating = [float(rating)]
        previous_user = user
    else:
        watched.append(int(movie))
        watched_rating.append(float(rating))

print(previous_user +'\t'+ str(watched) +'\t'+ str(watched_rating))
