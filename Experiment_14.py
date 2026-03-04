try:
    num1 = int(input("enter first value: "))
    num2 = int(input("enter second value: "))
    division = num1 / num2
except ZeroDivisionError:
    print("number cannot divide by zero")
except ValueError:
    print("invalid input")
else:
    print("ans:", division)
