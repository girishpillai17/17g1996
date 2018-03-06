import random
PassWord = str(random.randint(0,10))
Trial = ' '
while Trial != PassWord:
    Trial = str(random.randint(0,10))
    print(Trial)
    if Trial == PassWord:
        print('The password is: '+PassWord)
        input()