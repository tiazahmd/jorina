#! /usr/bin/python3.6

# Jorina is a command line assistant
# Version 1.0

import sys, json, requests
from modules import *

if len(sys.argv) < 2:
    error()
elif sys.argv[1] == "man":
    manual()
elif sys.argv[1] == "convert":
    try:
        convert(sys.argv[2], sys.argv[3])
    except IndexError:
        error()
elif sys.argv[1] == "weather":
    if len(sys.argv) == 2:
        city = "Salt Lake City"
        weather(city)
    elif len(sys.argv) > 2 and sys.argv[2] == "city":
        city = input("Enter city name: ")
        weather(city)
else:
    error()