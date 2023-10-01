#!/usr/bin/python3
"""takes in a URL and an email address, sends
a POST request to the passed URL with the email
as a parameter, and finally displays the body of
the response.
"""
import sys
import requests


def main():
    """takes in a URL and an email address, sends
    a POST request to the passed URL with the email
    as a parameter, and finally displays the body of
    the response.
    """
    url = sys.argv[1]
    data_up = {'email': sys.argv[2]}

    r = requests.post(url, data_up)

    print(r.text)


if __name__ == "__main__":
    main()
