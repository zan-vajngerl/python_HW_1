import keyboard
import time
from threading import Event
on = True

while True:

    first_number = int(input("Enter the first number: "))
    operator = input("Enter the operator (+,-,*,/): ")
    second_number = int(input("Enter the second number: "))

    if operator == "+":
        print (first_number + second_number)

    elif operator == "-":
        print (first_number - second_number)

    elif operator == "*":
        print (first_number * second_number)

    elif operator == "/":
        print (first_number / second_number)

    else: print("This calculator isn't advanced enough to support the desired operation")

    input("Press Enter to restart the calculator")
