#!/usr/bin/env python3
from sys import argv
if len(argv) == 2 and 'z' in argv[1]:
    print('z' * (argv[1].count('z')))
else:
    print('none')
