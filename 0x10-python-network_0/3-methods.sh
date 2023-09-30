#!/bin/bash
# get all methods
curl -sI "$1" | grep "^Allow" | awk -F ': ' '{print $2}'
