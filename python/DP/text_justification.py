""" 
    Text justification problem:
    
    Given an Array of words and a limit on the maximum number of words that
    can be put in one line (width of line). Put line breaks in a given 
    sequence such that the lines are printed neatly
"""

def greedy_algorithm(array, line_width):
    """ 
        Finds the lines and line breaks in O(n) time, may not be optimal 
        Returns a tuple of two Arrays.
        First Array contains the content of each line.
        Second Array contains the range of words present in a line.
    """
    if len(array) == 0:
        return ([], [])

    lines = []
    line_range = []
    start = 0
    string = ""
    i = 0

    while i < len(array):
        if len(string + array[i]) <= line_width:
            string += array[i] + " "
            i += 1
        else:
            lines.append(string[:-1])
            line_range.append((start, i-1))
            string = ""
            start = i

    lines.append(string[:-1])
    line_range.append((start, i-1))
    return (lines, line_range)
    
