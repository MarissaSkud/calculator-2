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

def subtract_multiples(nums_to_subtract):
    my_difference = nums_to_subtract[0]

    for i in range(1, len(nums_to_subtract)):
        my_difference -= nums_to_subtract[i]

    return my_difference

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
    if num2 == 0:
        return "You can't divide by zero"
    else:
        return num1 / num2

def divide_multiples(nums_to_divide):
    my_quotient = nums_to_divide[0]

    for i in range(1, len(nums_to_divide)):
        my_quotient /= nums_to_divide[i]
    
    return my_quotient

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
    if num2 == 0:
        return "You can't divide by zero"
    else:
        return num1 % num2
