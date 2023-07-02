#!/usr/bin/python3
""" Python modules """
import sys
import urllib.request

""" Script that takes in a URL, sends a request to the URL """

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(reeponse.headers).get("X-Request-Id")
