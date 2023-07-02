#!/bin/bash
# A script that take in a URL & displays al HTTP methods the server wil accept
curl -sI "$1" | grep -i "Allow" | awk -F ": " '{ print $2 }'
