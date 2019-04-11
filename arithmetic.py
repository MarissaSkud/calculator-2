"""Math functions for calculator."""


def add(num1, num2):
    """Return the sum of the two inputs."""

    return num1 + num2

def add_multiples(nums_to_add):
    my_sum = 0
    for num in nums_to_add:
        my_sum += num
    
    return my_sum

def subtract(num1, num2):
    """Return the second number subtracted from the first."""

    return num1 - num2

# def subtract_multiples(nums_to_subtract):
#     my_difference = nums_to_subtract[0]

#     for num in enumerate(nums_to_subtract, start = 1):
#         my_difference -= nums_to_subtract
#     # # i = 1

#     # for i in range(len(nums_to_subtract)-1):
#     #     my_difference -= nums_to_subtract[i+1]

#     return my_difference

# print(subtract_multiples([10, 5, 1]))

def multiply(num1, num2):
    """Multiply the two inputs together."""

    return num1 * num2

def multiply_multiples(nums_to_multiply):
    my_product = 1
    for num in nums_to_multiply:
        my_product *= num
    
    return my_product  

def divide(num1, num2):
    """Divide the first input by the second, returning a floating point."""

    return num1 / num2


# def divide_multiples(nums_to_divide):
#     my_quotient = nums_to_divide[0]

#     # for num in nums_to_subtract:
#     #     my_quotient /= 
    
#     return my_quotient

def square(num1):
    """Return the square of the input."""

    # Needs only one argument

    return num1 * num1


def cube(num1):
    """Return the cube of the input."""

    # Needs only one argument

    return num1 * num1 * num1


def power(num1, num2):
    """Raise num1 to the power of num and return the value."""

    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    """Return the remainder of num / num2."""

    return num1 % num2
