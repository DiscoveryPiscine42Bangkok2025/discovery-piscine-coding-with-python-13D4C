#!/usr/bin/env python3
import sys
def uwu(s):
    x = slice(8)
    print(s[x])
def ahhhh(s):
    print(s,'Z'*(8 - (len(s))),sep='')
argc = len(sys.argv)
argv = sys.argv
if argc >= 2:
    argv.pop(0)
    for i in range(len(argv)):
        if len(argv[i]) < 8:
            ahhhh(argv[i])
        else:
            uwu(argv[i])
else:
    print("none")