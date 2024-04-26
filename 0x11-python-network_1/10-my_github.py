#!/usr/bin/python3
"""Takes your GitHub credentials (username and password) and uses
the GitHub API to display your id."""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/user"
    usern = argv[1]
    token = argv[2]
    resp = requests.get(url, auth=(usern, token))
    print("{}".format(resp.json().get("id")))
