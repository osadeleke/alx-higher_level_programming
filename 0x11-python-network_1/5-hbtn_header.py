#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status
You must use the package requests
"""
import requests
import sys


def main():
    """fetches https://alx-intranet.hbtn.io/status
    You must use the package requests
    """
    r = requests.get(sys.argv[1])
    for key in r.headers:
        if key == 'X-Request-Id':
            val = r.headers['X-Request-Id']
            print(val)
            break


if __name__ == "__main__":
    main()
