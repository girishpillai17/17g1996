def remove_duplicates(list):
    new_list = []
    for element in list:
        if element not in new_list:
            new_list.append(element)
    print(new_list)

remove_duplicates([1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1,15,18,16,16])