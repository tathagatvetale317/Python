def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b 
def divide(a,b):
    return a / b
print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
Choice = int(input("Enter your choice (1-4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if Choice == 1:
    print("Result:", add(num1, num2))
elif Choice == 2:
    print("Result:", subtract(num1,num2))
elif Choice == 3:
    print("Result:", multiply(num1,num2))
elif Choice == 4:
    if num2 != 0:
        print("Result:", divide(num1,num2))
    else:
        print("Error: Division by zero")
else:
         print("Invalid choice")
