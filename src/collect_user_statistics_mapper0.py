#!/usr/bin/python3
import numpy
import sys

for line in sys.stdin:
    user, movie, rating, _ = line.strip().split(',')
    if user != 'userId':
        print('%s\t%s\t%s' % (user, movie, str(float(rating) / 5)))
