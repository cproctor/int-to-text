# int_to_text.py
# --------------
# Functions to print out a verbal representation of an integer.

MAXIMUM = 1000000

def int_under_1000000_to_text(number):
    "Returns a textual representation of the number."
    check_number_in_range(abs(number), 1 , MAXIMUM)
    return "A big number"
        
def int_under_1000_to_text(number):
    "Returns a textual representation of the number"
    check_number_in_range(number, 1, 1000)
    return "A big number"

def int_under_100_to_text(number):
    check_number_in_range(number, 1, 100)
    return "A big number"

def int_under_10_to_text(number):
    check_number_in_range(number, 1, 10)
    if number == 1:
        return "one"
    elif number == 2:
        return "two"
    elif number == 3:
        return "three"
    elif number == 4:
        return "four"
    elif number == 5:
        return "five"
    elif number == 6:
        return "six"
    elif number == 7:
        return "seven"
    elif number == 8:
        return "eight"
    elif number == 9:
        return "nine"

def check_number_in_range(number, minimum, maximum):
    if number < minimum:
        raise ValueError(f"{number} must not be below {minimum}.")
    if number >= maximum:
        raise ValueError(f"{number} must be less than {maximum}.")

def divide_with_remainder(dividend, divisor):
    """Divides one number by another, using whole-number division. 
    Returns the quotient and the remainder.
    Note how a function can return more than one value!
    """
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder
