import re

def adaptToNumber(strValue):
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
    digits = re.findall(r'\d+', strValue)
    
    print("Found digits: " + str(digits))
    
    return 42
    
