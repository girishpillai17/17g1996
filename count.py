def count(sequence, item):
    sum = 0                                 #set the counter as 0
    for num in sequence:
        if num == item:                     #checks if the element in sequence matches the item
            element = sequence.index(num)   #gives the index num
            sum = sum + 1                   #if found increases the count by 1
    print(sum)


count([3, 3, 7, 8, 9, 8, 2, 1, 2, 5, 6, 7, 4, 3, 2, 2, 2, 2, 1, 1], 2)