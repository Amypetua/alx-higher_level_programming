#!/bin/bash
# A script that takes in a URL, sends a request to it & displays the size.
curl -sI "$1" | awk '/Content-Length/{print $2}'
