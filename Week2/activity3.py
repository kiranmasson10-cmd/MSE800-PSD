class Calculator:
    """Performs basic math operations using OOP"""

    def __init__(self, num1, num2):  # Method 1: Constructor
        self.num1 = num1  # Instance attribute
        self.num2 = num2  # Instance attribute

    def add(self):  # Method 2
        return self.num1 + self.num2

    def subtract(self):  # Method 3
        return self.num1 - self.num2

    def multiply(self):  # Bonus method 4
        return self.num1 * self.num2

    def divide(self):  # Bonus method 5
        if self.num2 == 0:
            return "Error: Cannot divide by zero"
        return self.num1 / self.num2
def get_numbers():  # Function 1
    """Get user input and return two floats"""
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return get_numbers()  # Ask again

def display_results(calculator_obj):  # Function 2
    """Print all operation results using the Calculator object"""
    print(f"\nResults:")
    print(f"{calculator_obj.num1} + {calculator_obj.num2} = {calculator_obj.add()}")
    print(f"{calculator_obj.num1} - {calculator_obj.num2} = {calculator_obj.subtract()}")
    print(f"{calculator_obj.num1} * {calculator_obj.num2} = {calculator_obj.multiply()}")
    print(f"{calculator_obj.num1} / {calculator_obj.num2} = {calculator_obj.divide()}")
def main():
    print("=== OOP Calculator ===")
    num1, num2 = get_numbers()
    calc = Calculator(num1, num2)  # Create object from class
    display_results(calc)  # Pass object to function

if __name__ == "__main__":
    main()    
