
def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    else:
        return a / b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


result = divide_numbers(num1, num2)
print("The division of {} by {} is {}".format(num1, num2, result))
