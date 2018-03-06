def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def division(x , y):
    return x/y

def multiplication(x, y):
    return x * y

def modulus(x, y):
    return x % y

def fibonacci(x, y):
    a, b = 0, 1
    while (a+b) < x:
        print (a+b, end=' ')
        a, b = b, a+b
    print()
    a, b = 0, 1
    while (a + b) < y:
        print(a + b, end=' ')
        a, b = b, a + b


run = True

while run:

    print ("enter two numbers")
    num1 = int(input())
    num2 = int(input())

    print("""available operations:
        1 : addition
        2 : subtraction
        3 : division
        4 : multiplication
        5 : modulus
        6 : fibonacci""")

    choice = int(input())


    if choice == 0:
        print("goodbye human")
        run = False
    elif choice == 1:
        print(addition(num1, num2))
    elif choice == 2:
        print(subtraction(num1, num2))
    elif choice == 3:
        print(division(num1, num2))
    elif choice == 4:
        print(multiplication(num1, num2))
    elif choice == 5:
        print(modulus(num1, num2))
    elif choice == 6:
        print(fibonacci(num1,num2))
