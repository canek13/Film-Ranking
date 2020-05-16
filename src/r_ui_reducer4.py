#!/usr/bin/python3

"""
r_ui_reducer4
"""

import sys

previous_user = None
previous_film = None
numerator = 0
denumerator = 1

for line in sys.stdin:
    key, value = line.strip().split('\t',1)
    user, not_w = list(map(int, key.split(',')))
    sim, rank_w = list(map(float, value.split('\t')))
            
    if user != previous_user or not_w != previous_film:
        if previous_user: # if not None
            if denumerator != 0: # if denumerator not zero != 0 in predict for r_ui
                numerator /= denumerator
            else:
                numerator = 0
            print(str(previous_film) +','+ str(previous_user) +'\t'+
                str("{:.2f}".format(numerator)))
        numerator = sim * rank_w
        denumerator = sim
        previous_user = user
        previous_film = not_w
    else:
        numerator += sim * rank_w
        denumerator += sim
if denumerator != 0: # if denumerator not zero != 0 in predict for r_ui
        numerator /= denumerator
else:
    numerator = 0
print(str(previous_film) +','+ str(previous_user) +'\t'+
    str("{:.2f}".format(numerator)))
