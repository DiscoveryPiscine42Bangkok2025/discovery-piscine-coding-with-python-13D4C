want = 25
num = int(input())
if want > num:
    while True:
        if num <=want:
            print("e loop, my variable is",num)
        else:
            break
        num +=1
else:
    print("Error")
