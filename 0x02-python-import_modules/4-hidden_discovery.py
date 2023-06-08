#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    import sys
    atts = dir(hidden_4)
    for att in atts:
        if att[0] != '_':
            print(att)
