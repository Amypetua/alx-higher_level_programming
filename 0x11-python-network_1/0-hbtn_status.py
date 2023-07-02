#!/usr/bin/python3
"""
Python module for fetching URL
"""
import urllib.request

"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    request = urllib.request.Request(https://alx-intranet.hbtn.io/status)
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
