#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == {}:
        return None
    elif a_dictionary is not None:
        sort_scores = sorted(a_dictionary.values())
        i = sort_scores[len(sort_scores) - 1]
        for key, value in a_dictionary.items():
            if value == i:
                return key
    else:
        return None
