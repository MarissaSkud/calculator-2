"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from functools import reduce

from arithmetic import *

while True:

    user_input = input("> ")
    input_list = user_input.split(" ")

    float_list = []

    for i in range(1, len(input_list)):
        float_list.append(float(input_list[i]))

    # try:

    if input_list[0] == "q":
        break

    elif input_list[0] == "+":
        # print(add(num1, num2))
        my_sum = reduce((lambda num1,num2 : num1+num2), float_list)
        print(my_sum)

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

    else:
        print("Command not recognized")

    # except TypeError:
    #     print("This function needs a second number")
