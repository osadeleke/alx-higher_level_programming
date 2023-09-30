#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


def main():
    """Python script that fetches https://alx-intranet.hbtn.io/status
    """
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')

    with urllib.request.urlopen(req) as response:
        content_val = response.read()
        print('Body response:')
        print("\t- type: {}".format(type(content_val)))
        print("\t- content: {}".format(content_val))
        print("\t- utf8 content: {}".format(content_val.decode('utf-8')))


if __name__ == "__main__":
    main()
