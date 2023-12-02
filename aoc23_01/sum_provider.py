"""Computes the value sum for a calibration values file"""

import file_reader
import number_adapter


def get_sum(file_path):
    """
    Takes a calibration values file, computes the value from
    each line and returns the sum of those values.
    """

    lines = file_reader.read_lines(file_path)
    numbers = list(map(number_adapter.adapt_to_number, lines))

    return sum(numbers)
