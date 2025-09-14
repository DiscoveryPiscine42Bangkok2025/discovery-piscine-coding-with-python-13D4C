#!/usr/bin/env python3
import sys
def main():
    if len(sys.argv) != 3:
        print("Usage: ./your_script.py <number1> <number2>")
        return
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    except ValueError:
        print("Error: Both arguments must be valid integers.")
        return
    if num1 < num2:
        print(list(range(num1, num2 + 1)))
    elif num1 > num2:
        print(list(range(num1, num2 - 1, -1)))
    else:
        print([num1])
if __name__ == "__main__":
    main()