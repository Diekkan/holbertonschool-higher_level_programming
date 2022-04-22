#!/bin/bash
# Script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response
curl --head -s $1 2>&1 | grep 'Content-Length: ' | cut -d " " -f 2
