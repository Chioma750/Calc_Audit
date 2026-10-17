def main_menu():
    print("\n==== CALCULATOR MENU =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    options = input("Choose an option from the listed above: ").strip()
    return options

def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    return num1, num2

def main():
    while True:
        options = main_menu()

        if options == "5":
            print("Exiting...")
            break
        elif options in ("1", "2", "3", "4"):
            num1, num2 = calculator()

            if options == "1":
                print("Result: ", num1 + num2)
            elif options == "2":
                print("Result: ", num1 - num2)
            elif options == "3":
                print("Result: ", num1 * num2)
            elif options == "4":
                if num2 == 0:
                    print("Cannot divide by zero.")
                else:
                    print("Result: ", num1 / num2)
        else:
            print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")
if __name__ == "__main__":
    main()