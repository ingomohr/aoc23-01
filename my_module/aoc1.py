import fileReader
import numberAdapter
import functools

print("AOC 2023: Day 1: Trebuchet")
print("==========================")

lines = fileReader.readLines('data/input.txt')
length = len(lines)
print("Found lines: " + str(length));

# for each line call numberAdadapter.adaptToNumber

numbers = list(map(numberAdapter.adaptToNumber, lines))

print(numbers)



