def readLines(filePath):
    """
    Reads a file given given by its path and returns all lines.

    Parameters:
    filePath (str): The path to the file to be read.

    Returns:
    list: A list of strings where each string is a line from the file.
    """
    with open(filePath) as f:
        return f.readlines()
