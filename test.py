num1 = int(input("What is your first number: "))
num2 = int(input("What is your second number: "))
choice = input("choose an operator(+ or -): ")

if choice == "+":
    print("result: ", num1 + num2)
elif choice == "-":
    print("result: ", num1 - num2)
else:
    print("Invalid choice!")