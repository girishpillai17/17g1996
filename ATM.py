n, m = input().split(" ")
n = float(n)
m = float(m)
if (n + 0.50) >= m or n % 5 != 0:
    print("%0.2f" % m)
else:
    print("%0.2f" % (m - (n + 0.50)))
