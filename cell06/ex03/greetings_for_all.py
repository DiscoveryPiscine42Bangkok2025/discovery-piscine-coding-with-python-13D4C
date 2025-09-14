#!/usr/bin/env python3
def greetings(s=None):
    if s:
        if type(s) != str:
            print("Error! It was not a name.")
        else:
            print("Hello, " + s + ".")
    else:
        print("Hello, noble stranger.")
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)