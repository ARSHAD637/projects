num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Choose an operator: +, -, *, /")
operator = input("Enter the operator: ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2 if num2 != 0 else "Cannot divide by zero!"
else:
    result = "Invalid operator!"

print("Result:", result)




