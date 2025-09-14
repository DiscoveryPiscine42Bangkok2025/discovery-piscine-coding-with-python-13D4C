print("Enter a number")
num = int(input())
scale = 0
for i in range(10):
    print(scale,"x",num,"=",(scale*num))
    scale += 1
