#importing everything we need from colorama
from colorama import init 
from colorama import Fore, Back, Style

init()
print(Fore.BLUE)
#choosing the operator
operator = input ("Choose an operator (+, -, *, /, **)")
#choosing the numbers
num1 = float(input("Choose the first number:"))
num2 = float(input("Choose the second number:"))
#math calculations
if operator == "+":
    num3 = num1 + num2
    print("Result: " + str(num3))
elif operator == "-":
    num3 = num1 - num2
    print("Result: " + str(num3))
elif operator == "*":
    num3 = num1 * num2
    print("Result: " + str(num3))
elif operator == "/":
    num3 = num1 / num2
    print("Result: " + str(num3))
elif operator == "**":
    num3 = num1 ** num2
    print("Result: " + str(num3))
#incorrrect configuration
else:
    print(Fore.RED)
    print("Incorrect configuration!")
    
