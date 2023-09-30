#!/usr/bin/python3
import sys
import urllib.request
import urllib.error


def main():
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
