import math

def scientific_calculator():
    while True:
        print("\n===== SCIENTIFIC CALCULATOR =====")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (x^y)")
        print("6. Square Root")
        print("7. Sin")
        print("8. Cos")
        print("9. Tan")
        print("10. Log (base 10)")
        print("11. Natural Log (ln)")
        print("12. Factorial")
        print("13. Exit")

        choice = input("\nEnter your choice: ")

        try:
            if choice == "1":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result =", a + b)

            elif choice == "2":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result =", a - b)

            elif choice == "3":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result =", a * b)

            elif choice == "4":
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                if b == 0:
                    print("Error: Cannot divide by zero!")
                else:
                    print("Result =", a / b)

            elif choice == "5":
                a = float(input("Enter base: "))
                b = float(input("Enter power: "))
                print("Result =", a ** b)

            elif choice == "6":
                a = float(input("Enter number: "))
                print("Result =", math.sqrt(a))

            elif choice == "7":
                a = float(input("Enter angle in degrees: "))
                print("Sin =", math.sin(math.radians(a)))

            elif choice == "8":
                a = float(input("Enter angle in degrees: "))
                print("Cos =", math.cos(math.radians(a)))

            elif choice == "9":
                a = float(input("Enter angle in degrees: "))
                print("Tan =", math.tan(math.radians(a)))

            elif choice == "10":
                a = float(input("Enter number: "))
                print("Log =", math.log10(a))

            elif choice == "11":
                a = float(input("Enter number: "))
                print("ln =", math.log(a))

            elif choice == "12":
                a = int(input("Enter a positive integer: "))
                print("Factorial =", math.factorial(a))

            elif choice == "13":
                print("Calculator closed.")
                break

            else:
                print("Invalid choice! Please try again.")

        except ValueError:
            print("Error: Please enter a valid number.")
        except Exception as e:
            print("Error:", e)


scientific_calculator()
