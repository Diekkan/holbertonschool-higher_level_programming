#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept.
curl --head -s $1 2>&1 | grep 'Allow: ' | cut -d " " -f 2-
