#! /usr/bin/python3.6

# Jorina is a command line assistant
# Version 1.0

import sys
from modules import *

if len(sys.argv) < 2:
    error()
elif sys.argv[1] == "man":
    manual()
elif sys.argv[1] == "convert":
    convert(sys.argv[2], sys.argv[3])
else:
    error()