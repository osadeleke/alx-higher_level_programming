#!/usr/bin/python3
best_score = __import__('10-best_score').best_score

a_dictionary = {}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
