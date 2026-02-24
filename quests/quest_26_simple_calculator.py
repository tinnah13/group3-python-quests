# Simple Calculator
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b  
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
# Get user input for numbers and operation
num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ")
 
# Perform the calculation based on the operation
if operation == "add":
    result = add(num1, num2)
elif operation == "subtract":
    result = subtract(num1, num2)
elif operation == "multiply":
    result = multiply(num1, num2)
elif operation == "divide":
    result = divide(num1, num2)
else:
    result = "Invalid operation"   
# Print the result
print("The result is: ", result) 

    