#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    result_url = 'https://alx-intranet.hbtn.io/status'
    print("Body response:")
    print("\t- type: {}".format(type(requests.get(result_url).text)))
    print("\t- content: {}".format(requests.get(result_url).text))
