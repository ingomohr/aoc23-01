import functools
import file_reader
import number_adapter

print("AOC 2023: Day 1: Trebuchet")
print("==========================")

lines = file_reader.read_lines('data/input.txt')
length = len(lines)
print("Found lines: " + str(length))

# for each line call numberAdadapter.adaptToNumber

numbers = list(map(number_adapter.adapt_to_number, lines))

print(numbers)
