"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:

    num1 = None
    num2 = None

    user_input = input("> ")
    input_list = user_input.split(" ")

    try:
        num1 = float(input_list[1])
        num2 = float(input_list[2])
    except IndexError:
        pass

    # for index, num in enumerate(input_list, start=1):
    #     float_list.append(float(num))

    # print(float_list)

    try:

        if input_list[0] == "q":
            break

        elif input_list[0] == "+":
            print(add(num1, num2))

        elif input_list[0] == "-":
            print(subtract(num1, num2))

        elif input_list[0] == "*":
            print(multiply(num1, num2))

        elif input_list[0] == "/":
            print(divide(num1, num2))

        elif input_list[0] == "square":
            print(square(num1))

        elif input_list[0] == "cube":
            print(cube(num1))

        elif input_list[0] == "pow":
            print(power(num1, num2))

        elif input_list[0] == "mod":
            print(mod(num1, num2))

    except TypeError:
        print("This function needs a second number")
