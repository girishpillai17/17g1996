def fib(n):
    a, b = 0, 1
    while (a+b) < n:
        print (a+b, end=' ')
        a, b = b, a+b

fib(1000)

