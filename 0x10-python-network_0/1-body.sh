#!/bin/bash
# return only 200 status code body
if [ $(curl -s -o /dev/null -w "%{http_code}" "$url") == 200 ]; then curl -s $1
fi
