def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def modulus(a, b):
    if isinstance(a, complex) or isinstance(b, complex):
        return "Error: Modulus not supported for complex numbers"
    if b == 0:
        return "Error: Cannot divide by zero"
    return a % b

def factorial(n):
    if isinstance(n, complex) or not float(n).is_integer() or n < 0:
        return "Error: Factorial only defined for non-negative integers"
    n = int(n)
    return 1 if n == 0 else n * factorial(n-1)

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Factorial")

choice = input("Enter choice (1-6): ")

if choice == '6':
    num = float(input("Enter a number: "))
    print("Result:", factorial(num))
else:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    try:
        num1 = complex(num1)
    except ValueError:
        num1 = float(num1)

    try:
        num2 = complex(num2)
    except ValueError:
        num2 = float(num2)

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", modulus(num1, num2))
    else:
        print("Invalid choice")