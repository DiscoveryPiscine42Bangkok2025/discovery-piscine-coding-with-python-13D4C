first = int(input())
second = int(input())
num = first*second
print(first,"x",second,"=",num)
if num == 0:
    print("This result is both positive and negative.")
elif num > 0:
    print("This result is positive.")
elif num < 0 :
    print("This result is negative.")