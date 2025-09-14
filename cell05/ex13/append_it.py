#!/usr/bin/env python3
from sys import argv
def main():
    if len(argv) >= 2:
        for txt in argv[1:]:
            if not txt.endswith('ism'):
                if txt.endswith('e'):
                    txt = txt[:-1] + 'ism'
                else:
                    txt = txt + 'ism'
            print(txt)
    else:
        print('none')
if __name__ == "__main__":
    main()