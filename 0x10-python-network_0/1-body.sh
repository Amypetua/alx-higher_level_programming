#!/bin/bash
# A script that takes in a URL, sends a GET request to it, & displays the body
curl -Lsf "$1"
