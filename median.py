def median(lst):
    sorted_lst = sorted(lst)
    lstlen = len(lst)
    index = (lstlen-1) // 2
    if lstlen%2 != 0:
        print(sorted_lst[index])
    else:
        print((sorted_lst[index] + sorted_lst[index+1])/2.0)



median([1])