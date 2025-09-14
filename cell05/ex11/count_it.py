#!/usr/bin/env python3
from sys import argv
if len(argv) >= 2:
    print('parameters:', len(argv) - 1)
    for txt in argv[1:]:
         print(f'{txt}: {len(txt)}')
else:
    print('none')
