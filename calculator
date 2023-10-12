
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def logarithm(x, base):
    return math.log(x, base)

# Main calculator loop
while True:
    print("Scientific Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("0. Exit")

    choice = input("Enter your choice (0-7): ")

    if choice == '0':
        print("Exiting the calculator...")
        break

    if choice in ['1', '2', '3', '4', '5', '7']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            result = add(num1, num2)
            print("Result: ", result)
        elif choice == '2':
            result = subtract(num1, num2)
            print("Result: ", result)
        elif choice == '3':
            result = multiply(num1, num2)
            print("Result: ", result)
        elif choice == '4':
            result = divide(num1, num2)
            print("Result: ", result)
        elif choice == '5':
            result = power(num1, num2)
            print("Result: ", result)
        elif choice == '7':
            result = logarithm(num1, num2)
            print("Result: ", result)

    elif choice == '6':
        num = float(input("Enter the number: "))
        result = square_root(num)
        print("Result: ", result)

    else:
        print("Invalid choice. Please try again.")
