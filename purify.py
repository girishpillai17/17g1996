def purify(num):
    for number in num[:]:
        if number%2 != 0:
            num.remove(number)
    print(num)




purify([1,8,9,6,5,3,4,6,5,8,8,9,9,2,3,1,5])
