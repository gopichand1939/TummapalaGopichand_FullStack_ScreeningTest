# Problem-1.py

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self, operation):
        if operation == "add":
            return self.a + self.b
        elif operation == "subtract":
            return self.a - self.b
        elif operation == "multiply":
            return self.a * self.b
        elif operation == "divide":
            if self.b == 0:
                return "Cannot divide by zero"
            return self.a / self.b
        else:
            return "Unsupported operation"

# inputs accepting
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (add/subtract/multiply/divide): ").lower()

calc = Calculator(num1, num2)
result = calc.calculate(op)
print("Result:", result)
