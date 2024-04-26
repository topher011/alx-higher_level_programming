#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
"""
from urllib.request import Request, urlopen
from sys import argv

if __name__ == "__main__":
    with urlopen(Request(argv[1])) as resp:
        print(resp.headers.get('X-Request-Id'))
