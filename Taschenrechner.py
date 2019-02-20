import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def main():

    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Pull the root")
    print("6.Square")

    choice = input("Enter 1/2/3/4/5/6: ")
    if choice == '5':
        num1 = int(input("Enter number: "))

    elif choice == '6':
        print()
        print("Select operation.")
        print("1.Squared by 2")
        print("2.Squared by 3")
        choice2 = input("Enter 1/2: ")
        if choice2 == '1':
            num1 = int(input("Enter number: "))

        elif choice2 == '2':
            num1 = int(input("Enter number: "))

        else:
            print("Invalid input")

    else:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))

    elif choice == '5':
        print("\u221A", num1, "=", math.sqrt(num1))

    elif choice == '6' and choice2 == '1':
        print(num1, "^", "2", "=", num1**2)

    elif choice == '6' and choice2 == '2':
        print(num1, "^", "3", "=", num1**3)

    else:
        print("Invalid input")

    print()
    restart = input("More calculation? Type in y/n: ")

    if restart == 'y':
        main()

    else:
        exit()


print("Hey! This is my first python project. It´s more an copy of an online source code,")
print("but the repeating part is my own creation :D")
print()
main()
