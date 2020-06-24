operator = input ("Choose an operator (+, -, *, /, **)")

a = float(input("Choose the first number:"))
b = float(input("Choose the second number:"))

if operator == "+":
    c = a + b
    print("Result: " + str(c))

elif operator == "-":
    c = a - b
    print("Result: " + str(c))
elif operator == "*":
    c= a * b
    print("Result: " + str(c))
elif operator == "/":
    c= a / b
    print("Result: " + str(c))
elif operator == "**":
    c = a ** b 
    print("Result: " + str(c))
else:
    print("Incorrect configuration!")
    