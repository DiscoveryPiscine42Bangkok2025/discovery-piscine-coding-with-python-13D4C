import sys

if len(sys.argv) > 1:
    print("none")
else:
    for i in range(11):
        num = [str(i * j) for j in range(11)]
        print(f"Table de {i}: {' '.join(num)}")