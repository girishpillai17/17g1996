def is_even(num):
    even = []
    for number in num:
        if number%2 == 0:
            even.append(number)
    print("even= %s" %even)


is_even([1,2,3,4,5,6,7,8,9])

def is_odd(num):
    odd = []
    for i in num:
        if i%2 != 0:
            odd.append(i)
    print("odd = %s" %odd)

is_odd([1,2,3,4,5,6,7,8,9])


