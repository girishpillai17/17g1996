x = int(input())
a = []
for i in range(x):
    n = int(input())
    a.append(n)
a.sort()
for j in range(x):
    print(a[j])