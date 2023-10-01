#!/usr/bin/python3
"""takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter
as a parameter.
"""
import requests
import sys


def main():
    """takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the letter
    as a parameter.
    """
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) < 2:
        data_load = {'q': ""}
    else:
        data_load = {'q': sys.argv[1]}

    r = requests.post(url, data_load)

    try:
        r_dumped = r.json()
    except ValueError as e:
        print("Not a valid JSON")
        return

    if len(r_dumped) == 0:
        print("No result")
        return

    print("[{}] {}".format(r_dumped['id'], r_dumped['name']))


if __name__ == "__main__":
    main()
