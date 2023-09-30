#!/usr/bin/python3
"""Python script that fetches a variable from header
"""
import sys
import urllib.request
import urllib.error


def main():
    """Python script that fetches a variable from header
    """
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            this_page = response.read().decode('utf-8')
            print(this_page)
    except urllib.error.HTTPError as e:
        print("Error code: {}"format(e.code))


if __name__ == "__main__":
    main()
