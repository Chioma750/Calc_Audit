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
    print("Invalid operator, choose either +, -, * or /.")

def main_menu():
    print("==== CALCULATOR MENU =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    options = input("Choose an option: ")