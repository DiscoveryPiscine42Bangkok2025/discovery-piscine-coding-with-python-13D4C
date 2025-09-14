#!/usr/bin/env python3
from sys import argv
if len(argv) == 2:
    txt = input('What was the parameter? ')
    if txt == argv[1]:
        print('Good job!')
    else:
        print('Nope, sorry...')
else:
    print('none')