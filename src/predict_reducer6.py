#!/usr/bin/python3

import sys

previous_user = None
previous_film = None

top_film = []
top_rating = []

for line in sys.stdin:
    user, not_w, rating = line.strip().split('\t')
    #key, rating = line.strip().split('\t')
    #user, not_w = key.split(',', 1)
    user = int(user)
    rating = float(rating) * 5

    if user != previous_user:
        if previous_user:
            #output top 3 films indexes and their ratings
            top = list(zip(top_rating, top_film))
            top = sorted(sorted(top, key=lambda x: x[1]), key=lambda x: x[0], reverse=True)[:3]
            print(str(previous_user) +'\t'+ str(top))

        previous_film = not_w
        previous_user = user
        # renew statistics
        top_film = [not_w]
        top_rating = [rating]

    elif not_w != previous_film:
        top_film.append(not_w)
        top_rating.append(rating)

top = list(zip(top_rating, top_film))
top = sorted(sorted(top, key=lambda x: x[1]), key=lambda x: x[0], reverse=True)[:3]
print(str(previous_user) +'\t'+ str(top))
