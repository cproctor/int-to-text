# int_to_text.py
# --------------
# Functions to print out a verbal representation of an integer.

MAXIMUM = 1000000

def int_under_1000000_to_text(number):
    "Returns a textual representation of the number."
    check_number_in_range(abs(number), 1 , MAXIMUM)
    if number < 1000:
        return int_under_1000_to_text(number)
    else:
        thousands, hundreds = divide_with_remainder(number, 1000)
        thousands_text = int_under_1000_to_text(thousands)
        hundreds_text = int_under_1000_to_text(hundreds)
        return thousands_text + " thousand " + hundreds_text
        
def int_under_1000_to_text(number):
    "Returns a textual representation of the number"
    check_number_in_range(number, 1, 1000)
    if number < 100:
        return int_under_100_to_text(number)
    else:
        hundreds, tens = divide_with_remainder(number, 100)
        hundreds_text = int_under_10_to_text(hundreds)
        tens_text = int_under_100_to_text(tens)
        return hundreds_text + " hundred and " + tens_text

def int_under_100_to_text(number):
    check_number_in_range(number, 1, 100)
    if number < 10:
        return int_under_10_to_text(number)
    else:
        tens, ones = divide_with_remainder(number, 10)
        if tens == 9: 
            return "ninety-" + int_under_10_to_text(ones)
        elif tens == 8:
            return "eighty-" + int_under_10_to_text(ones)
        elif tens == 7:
            return "seventy-" + int_under_10_to_text(ones)
        elif tens == 6:
            return "sixty-" + int_under_10_to_text(ones)
        elif tens == 5:
            return "fifty-" + int_under_10_to_text(ones)
        elif tens == 4:
            return "forty-" + int_under_10_to_text(ones)
        elif tens == 3:
            return "thirty-" + int_under_10_to_text(ones)
        elif tens == 2:
            return "twenty-" + int_under_10_to_text(ones)
        elif number >= 16:
            return int_under_10_to_text(ones) + "teen"
        elif number == 15:
            return "fifteen"
        elif number == 13:
            return "fourteen"
        elif number == 13:
            return "thirteen"
        elif number == 12:
            return "twelve"
        elif number == 11:
            return "eleven"

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
