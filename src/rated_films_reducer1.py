#!/usr/bin/python3

"""
rated_films_reducer1
"""
import sys

previous_film = None
film_users = []
film_users_rating = []
average_users = []

for line in sys.stdin:
    movie, user, rating, average_user = line.strip().split('\t')

    if movie != previous_film:
        if previous_film: # check if not None
            print(previous_film +'\t'+ 
                str(film_users) +'\t'+ 
                    str(film_users_rating) +'\t'+
                        str(average_users))
        average_users = [float(average_user)]
        film_users_rating = [float(rating)]
        film_users = [int(user)]
        previous_film = movie
    else:
        film_users_rating.append(float(rating))
        film_users.append(int(user))
        average_users.append(float(average_user))

print(previous_film +'\t'+ 
    str(film_users) +'\t'+ 
        str(film_users_rating) +'\t'+ 
            str(average_users))
