def censor(text, word):
    text = text.lower() #converts upper case leters to lowercase
    word = word.lower() #converts uppercase to lower case
    words = text.split() #seperates the string with list of words
    replace = '*' * len(word) #makes a string == word size
    count = 0 #elments in the list starts with 0
    for w in words:
        if w == word:
            words[count] = replace #if i mathches with word then that element is replaced with **..
        count = count + 1 #count is increased so that next element is compared
    result = " ".join(words) #we had convereted string to list so we join the list again to convert into string
    print(result)

censor("hey get the fuck out of here", "fuck")

