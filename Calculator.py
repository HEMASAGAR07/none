

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero."

def exponentiate(a, b):
    return a ** b

def modulo(a, b):
    return a % b

def floor_divide(a, b):
    if b != 0:
        return a // b
    else:
        return "Cannot divide by zero."

result = None

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")
    print("6. Modulo")
    print("7. Floor Divide")
    print("8. Clear Result")
    print("9. Exit")

    choice = input("Enter choice: ")

    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        if result is not None:
            num1 = result
            num2 = float(input("Enter number: "))
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        elif choice == '5':
            result = exponentiate(num1, num2)
        elif choice == '6':
            result = modulo(num1, num2)
        elif choice == '7':
            result = floor_divide(num1, num2)

        print("Result:", result)

    elif choice == '8':
        result = None
        print("Result cleared.")

    elif choice == '9':
        break

    else:
        print("Invalid input")
