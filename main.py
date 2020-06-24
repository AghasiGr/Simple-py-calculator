from colorama import init 
from colorama import Fore, Back, Style

init()
print(Fore.BLUE)
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
    print(Fore.RED)
    print("Incorrect configuration!")
    
