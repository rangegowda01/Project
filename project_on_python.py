# -*- coding: utf-8 -*-

"""   Mini project on python   """



def prompt_menu():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
 # choose the operation additon or subtraction etc
    print("""
Choose an operation from the list :
1. Addition
2. Subtraction
3. Multiplication
4. Exponentiation
5. Division
6. Division with remainder
    """)
    opt = int(input("Enter the choice number: "))
    return a, b, opt

def calculate():         # defining the calculate for the operation we select
    a, b, opt = prompt_menu()
    if opt == 1:
        print("Sum : {} + {} = {}".format(a,b,a+b))
    elif opt == 2:
        print("Difference : {} - {} = {}".format(a,b,a-b))
    elif opt == 3:
        print("Product : {} * {} = {}".format(a,b,a*b))
    elif opt == 4:
        print("Power : {}^{} = {}".format(a,b,a**b))
    elif opt == 5:
        try:
            print("Quotient : {} / {} = {}".format(a,b,a/b))
        except:
            print("Division by 0 not possible")
    elif opt == 6:
        try:
            print("Division with remainder : {} / {} = {} Remainder : {}".format(a,b,a//b,a%b))
        except:
            print("Divsion by 0 not possible")
    else:
        print("No such choice")
    loop()
 # to continue the calculate defining the loop
def loop():
    choice = input("Do you want to continue? (Y,N) : ")
    if choice.upper() == "Y":
        calculate()
    elif choice.upper() == "N":
        print("Good bye")
    else:
        print("Invalid input")
        loop()

calculate()
