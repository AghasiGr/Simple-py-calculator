#importing everything we need from colorama
from colorama import init 
from colorama import Fore, Back, Style

init()
print(Fore.BLUE)
#choosing the operator
operator = input ("Choose an operator (+, -, *, /, **)")
#choosing the numbers
a = float(input("Choose the first number:"))
b = float(input("Choose the second number:"))
#math calculations
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
#incorrrect configuration
else:
    print(Fore.RED)
    print("Incorrect configuration!")
    
