#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse


def main():
    """Takes in a URL and an email, sends a POST request
    to the passed URL with the email as a parameter, and
    displays the body of the response (decoded in utf-8)
    """
    url = sys.argv[1]
    val = {'email': sys.argv[2]}

    val_enc = urllib.parse.urlencode(val)
    val_enc = val_enc.encode('ascii')

    req = urllib.request.Request(url, val_enc)

    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode('utf-8')
        print(the_page)


if __name__ == '__main__':
    main()
