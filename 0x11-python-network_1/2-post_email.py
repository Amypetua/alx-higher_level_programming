#!/usr/bin//python3
""" Python modules """
import sys
import urllib.request
import urllib.parse
""" A Python script that takes in a URL, sends a request to the URL """


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
