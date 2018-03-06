def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                print("composite")
                print( i,"times",x//i,"is",x )
                break
        else:
            print("prime")
