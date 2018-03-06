Test = int(input())
for i in range(Test):
    n = input()
    no_4  = 0
    for i in range(len(n)):
        if n[i] == "4":
            no_4 += 1
    print(no_4)
