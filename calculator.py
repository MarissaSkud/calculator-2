"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True:
    user_input = input("> ")
    input_list = user_input.split(" ")

    if input_list[0] == "q":
        break

    elif input_list[0] == "+":
        num1 = float(input_list[1])
        num2 = float(input_list[2])
        print(add(num1, num2))

    elif input_list[0] == "-":
        num1 = float(input_list[1])
        num2 = float(input_list[2])
        print(subtract(num1, num2))

    elif input_list[0] == "*":
        num1 = float(input_list[1])
        num2 = float(input_list[2])
        print(multiply(num1, num2))

    elif input_list[0] == "/":
        num1 = float(input_list[1])
        num2 = float(input_list[2])
        print(divide(num1, num2))

    elif input_list[0] == "square":
        num1 = float(input_list[1])
        print(square(num1))

    elif input_list[0] == "cube":
        num1 = float(input_list[1])
        print(cube(num1))

    elif input_list[0] == "pow":
        num1 = float(input_list[1])
        num2 = float(input_list[2])
        print(power(num1, num2))

    elif input_list[0] == "mod":
        num1 = float(input_list[1])
        num2 = float(input_list[2])
        print(mod(num1, num2))
