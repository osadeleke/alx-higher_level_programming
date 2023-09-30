#!/usr/bin/python3
"""Python script that fetches a variable from header
"""
import urllib.request
import sys


def main():
    """Python script that fetches a variable from header
    """
    url = sys.argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        content_val = response.info()['X-Request-Id']
        print(content_val)


if __name__ == "__main__":
    main()
