r = int(input()) #takes the number of elements to remove the factorial

for i in range(r):
    n = int(input())
    fact = 1     #set fact as one so it can be multiplied by consecutive number
    while n >= 1: #for eg if we want to find factorial of 3 then range will be 1-3 as 3*2*1
        fact = fact * n
        n -= 1  #decrement n by 1
    print(fact)