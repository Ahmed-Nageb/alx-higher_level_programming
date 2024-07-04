#!/bin/bash
# Bash script takes URL, sends a request that URL & displays the size
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
