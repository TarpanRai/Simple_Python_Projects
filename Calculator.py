# Simple text based calculator with add, subtract, multiply, divide

# Function to add
def addition(num1, num2):
    return num1 + num2

# Function to subtract
def subtraction(num1, num2):
    return num1 - num2

# Function to multiply
def multiply(num1, num2):
    return num1 * num2

# Function to divide
def divide(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero"
    else:
        return num1 / num2


def main():
    print("----------------Calculator----------------")

    # Dictionary to map user input to functions
    operation_dict = {
        '1': addition,
        '2': subtraction,
        '3': multiply,
        '4': divide
    }

    while True:
        # Display menu
        print("\nOptions:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Type 1-5:")

        # Exit app
        if choice == '5':
            print("Good Bye!")
            break

        # Get user input
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))

        selected_operation = operation_dict.get(choice)

        if selected_operation:
            result = selected_operation(num1, num2)
            print("\nOutput: ", result)
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == '__main__':
    main()
