# calculator.py

# --- Step 1: Define functions for each operation ---
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b


# --- Step 2: Display menu and get user choice ---
def show_menu():
    print("\n----- Simple Calculator -----")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("-----------------------------")


# --- Step 3: Main loop for calculator ---
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting... Thank you for using the calculator!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Please enter a number between 1 and 5.")
            continue

        # Take user input for numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        # Perform operation based on user choice
        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")


# --- Step 4: Run the calculator ---

if __name__ == "__main__":
    main()
