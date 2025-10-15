print("Welcome to the Simple Calculator!")


def simpleCalculator():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    try:
        user_choice = int(input("Please choose an option: "))
        flag = False
        while not flag:
            if user_choice == 1:
                number1 = int(input("Enter the first number: "))
                number2 = int(input("Enter the second number: "))
                result = number1 + number2
                print(f"Result: {result}")
            elif user_choice == 2:
                number1 = int(input("Enter the first number: "))
                number2 = int(input("Enter the second number: "))
                result = number1 - number2
                print(f"Result: {result}")
            elif user_choice == 3:
                number1 = int(input("Enter the first number: "))
                number2 = int(input("Enter the second number: "))
                result = number1 * number2
                print(f"Result: {result}")
            elif user_choice == 4:
                number1 = int(input("Enter the first number: "))
                number2 = int(input("Enter the second number: "))
                result = number1 / number2
                print(f"Result: {int(result)}")
            elif user_choice == 5:
                print("Goodbye!")
                flag = True
    except ValueError:
        print("Please enter a valid number")


simpleCalculator()