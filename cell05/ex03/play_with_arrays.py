arr = [2, 8, 9, 48, 8, 22, -12, 2]
new = set()
for i in range(len(arr)):
    if arr[i] > 5:
        new.add(arr[i] + 2)
print(arr)
print(new)