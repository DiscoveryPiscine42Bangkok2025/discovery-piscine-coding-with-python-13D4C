#!/usr/bin/env python3
from sys import argv
class eiei():
    def main(txt):
        if len(argv) >= 2:
            lst = [i.lower() for i in txt]
            print(*lst, sep='\n')
        else:
            print('none')
downcase_it = eiei.main

downcase_it(argv[1:])