""" Adapts strings to 2-digit numbers """

import re


def adapt_to_number(str_value):
    """
    From https://adventofcode.com/2023/day/1

    "...calibration value can be found by combining the first
    digit and the last digit (in that order) to form a single
    two-digit number."

    Parameters:
    strValue (str): value that is supposed to contain 1 first and a last digit

    Returns:
    list: A list of strings where each string is a line from the file.

    """

    # find all digits in string
    digits = re.findall(r'\d', str_value)

    if len(digits) < 1:
        raise ValueError("Line must contain 2 or more digits: " + str_value)

    d1 = digits[0]
    d2 = digits[len(digits) - 1]

    return int(str(d1) + str(d2))
