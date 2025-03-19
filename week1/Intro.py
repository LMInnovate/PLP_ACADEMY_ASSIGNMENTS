#Instructions:Basic Calculator ProgramCreate a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).Perform the operation based on the user's input and print the result.Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.
# Basic Calculator Program

# Ask for user input
number1 = float(input("Enter the first number:"))
number2 = float(input("Enter the second number:"))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation and display the result
if operation == '+':
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")
elif operation == '-':
    result = number1 - number2
    print(f"{number1} - {number2} = {result}")
elif operation == '*':
    result = number1 * number2
    print(f"{number1} * {number2} = {result}")
elif operation == '/':
    if number2 != 0:
        result = number1 / number2
        print(f"{number1} / {number2} = {result}")
    else:
        print("Program exited with Error: Division by zero is not allowed.")
else:
    print("Invalid Arithmetic operation. Please enter one of +, -, *, or /.")

