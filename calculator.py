"""git-calculator: a simple command-line calculator."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b


# Menu options: key -> (label, function)
OPERATIONS = {
    "1": ("Add", add),
    "2": ("Subtract", subtract),
    "3": ("Multiply", multiply),
    "4": ("Divide", divide),
}


def show_menu():
    print("\n=== Git Calculator ===")
    for key, (label, _) in OPERATIONS.items():
        print(f"{key}. {label}")
    print("q. Quit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip().lower()

        if choice == "q":
            print("Goodbye!")
            break

        if choice not in OPERATIONS:
            print("Invalid choice, try again.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        label, operation = OPERATIONS[choice]
        print(f"{label} result: {operation(a, b)}")


if __name__ == "__main__":
    main()
