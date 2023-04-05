# Made with PyCharm by Vincent

num1 = 0
num2 = 0
result = 0
factResult = 0
userChoice = 0
operations = [1, 2, 3, 4, 5, 6]
calculateAgain = ""


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


def exponent(num1, num2):
    return num1**num2


def factorial(num1):
    factorialResult = 1
    for i in range(2, num1 + 1):
        factorialResult *= i
    return factorialResult


while True:
    print("Select an operation to calculate with.")
    print(
        " 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Exponentiation \n 6. Factorial"
    )
    userChoice = ""

    try:
        while userChoice not in operations:
            userChoice = int(input("Selection: "))
            if userChoice not in operations:
                print("Invalid selection!")
    except ValueError:
        print("Invalid selection!")

    # Addition
    if userChoice == 1:
        print("Enter two integers to add together.")
        while True:
            try:
                num1 = int(input("First number: "))
                num2 = int(input("Second number: "))
                result = addition(num1, num2)
            except ValueError:
                print("Please input integers only!")
            else:
                break
        print(str(num1) + " + " + str(num2) + " = " + str(result))

    # Subtraction
    if userChoice == 2:
        print("Enter two integers to subtract.")
        while True:
            try:
                num1 = int(input("First number: "))
                num2 = int(input("Second number: "))
                result = subtraction(num1, num2)
            except ValueError:
                print("Please input integers only!")
            else:
                break
        print(str(num1) + " - " + str(num2) + " = " + str(result))

    # Multiplication
    if userChoice == 3:
        print("Enter two integers to multiply.")
        while True:
            try:
                num1 = int(input("First number: "))
                num2 = int(input("Second number: "))
                result = multiplication(num1, num2)
            except ValueError:
                print("Please input integers only!")
            else:
                break
        print(str(num1) + " x " + str(num2) + " = " + str(result))

    # Division
    if userChoice == 4:
        print("Enter two integers to divide.")
        while True:
            try:
                num1 = int(input("Numerator: "))
                num2 = int(input("Denominator: "))
                result = division(num1, num2)
            except ValueError:
                print("Please input integers only!")
            except ZeroDivisionError:
                print("Cannot divide by 0!")
            else:
                break
        print(str(num1) + " / " + str(num2) + " = " + str(result))

    # Exponentiation
    if userChoice == 5:
        print("Enter two integers for exponentiation.")
        while True:
            try:
                num1 = int(input("Enter a number: "))
                num2 = int(input("Enter an exponent: "))
                result = exponent(num1, num2)
            except ValueError:
                print("Please input integers only!")
            else:
                break
        print(str(num1) + " ^ " + str(num2) + " = " + str(result))

    # Factorization
    if userChoice == 6:
        print("Enter a number to factorize.")
        while True:
            try:
                num1 = int(input("Factorized number: "))
                result = factorial(num1)
            except ValueError:
                print("Please input integers only!")
            else:
                break
        print(str(num1) + "!" + " = " + str(result))
    while calculateAgain == "Y" or "N":
        calculateAgain = input("Would you like to calculate again? (Y/N): ").upper()
        if calculateAgain == "Y":
            break
        elif calculateAgain == "N":
            print("Goodbye!")
            exit()
