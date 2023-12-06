""" Main program """

from src import sum_provider


def main():
    """
    Main method of the program. Reads the input file and prints the result.
    """

    print("AOC 2023: Day 1: Trebuchet")
    print("==========================")

    result = sum_provider.get_sum('data/input.txt')
    print("Computed sum: " + str(result))


if __name__ == '__main__':
    main()
