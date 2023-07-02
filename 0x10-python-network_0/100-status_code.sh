#!/bin/bash
# A script that sends request to a URL passed as an argument & display status
curl -s -o /dev/null -w "%{http_code}" "$1"
