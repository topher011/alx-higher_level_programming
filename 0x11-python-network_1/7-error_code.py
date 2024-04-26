#!/usr/bin/python3
""" Takes in a URL, sends a request to the URL and displays
the body of the response.(error text) """
import requests
import sys

if __name__ == "__main__":
    resp = requests.get(sys.argv[1])

    if str(resp.status_code)[0] == '2':
        print(resp.text)
    else:
        print("Error code: {}".format(resp.status_code))
