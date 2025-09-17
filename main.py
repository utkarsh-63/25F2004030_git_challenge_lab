def sum_numbers(a, b):
    return a + b

def difference_numbers(a, b):
    return a - b

def product_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b

def main():
    while True:
        print("\nSimple Arithmetic Operations")
        print("1. Sum")
        print("2. Difference")
        print("3. Product")
        print("4. Division")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '5':
            print("Exiting the program.")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid option. Please choose a valid one.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            print(f"Sum: {sum_numbers(num1, num2)}")
        elif choice == '2':
            print(f"Difference: {difference_numbers(num1, num2)}")
        elif choice == '3':
            print(f"Product: {product_numbers(num1, num2)}")
        elif choice == '4':
            print(f"Division: {divide_numbers(num1, num2)}")

if __name__ == "__main__":
    main()

