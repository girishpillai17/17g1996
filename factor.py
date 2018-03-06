t = int(input())  #takes the num of numbers to be excuted

for i in range(t):
    x = int(input()) #takes the desired num
    a = x // 5
    z = a
    while a >= 5:
        a = a // 5
        z = z + a
    print(z)
