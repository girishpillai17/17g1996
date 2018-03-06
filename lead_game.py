x = int(input())
p1 = 0
p2 = 0
list = [0, 0]
for i in range(x):
    p1 = 0
    p2 = 0
    y, z = map(int, input().split(" "))
    p1 += y
    p2 += z
    if p1 - p2 > 0 and p1 - p2 > list[1]:
        list[1] = p1 - p2
        list[0] = 1
    elif p2 - p1 > 0 and p2-p1 > list[1]:
        list[1] = p2 - p1
        list[0] = 2
print(list[0], list[1])
