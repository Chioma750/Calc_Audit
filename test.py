# A SIMPLE CALCULATOR
num1 = float(input("Enter first number: "))
operator = input("Enter operator(*, +, -, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result: ", num1 + num2)
elif operator == "-":
    print("Result: ", num1 - num2)
elif operator == "*":
    print("Result: ", num1 * num2)
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        print("Result: ", num1 / num2)
else:
    print("Invalid operator")

# JUST ADD OR MINUS
num1 = int(input("What is your first number: "))
num2 = int(input("What is your second number: "))
choice = input("choose an operator(+ or -): ")

if choice == "+":
    print("result: ", num1 + num2)
elif choice == "-":
    print("result: ", num1 - num2)
else:
    print("Invalid choice!")
