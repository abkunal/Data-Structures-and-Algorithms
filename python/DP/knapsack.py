""" 0/1 Knapsack Problem using Dynamic Programming """

import unittest

def knapsack(val, wt, total):
    """
        val: array pf values of items
        wt: array of weights of items
        total: maximum weight capacity of knapsack
        Find which items to include in order to maximize value.
    """
    if len(val) != len(wt):
        raise "Error: Length of value array and weight array are different"
    elif len(val) == 0 or len(wt) == 0 or total == 0:
        return 0
        
    T = [[0 for i in range(total+1)] for j in range(len(val))]

    for i in range(len(val)):
        for j in range(1, total+1):
            if j < wt[i]:
                try:
                    T[i][j] = T[i-1][j]
                except IndexError:
                    T[i][j] = 0
            else:
                try:
                    T[i][j] = max(val[i] + T[i-1][j-wt[i]], T[i-1][j])
                except IndexError:
                    T[i][j] = val[i]
    print_path(wt, T)
    print("Maximum value: ", T[-1][-1])
    return T[-1][-1]


def print_path(wt, T):
    """ Print which items to pick """
    i = len(T) - 1
    j = len(T[0]) - 1

    # stores the indices of the items to pick
    items = []
    while i >= 0 and j >= 0:
        if T[i][j] == T[i][j-1]:
            i -= 1
        else:
            items.append(i-1)
            i -= 1
            try:
                j = j - T[i-1][j-wt[i]]
            except IndexError:
                break
    
    print("Pick items with indices: ", end=" ")
    for item in items:
        print(item, end=" ")
    print()


class TestKnapsack(unittest.TestCase):
    """ Test Cases for knapsack function """

    def test_empty_array(self):
        assert knapsack([], [], 100) == 0
        assert knapsack([], [], 0) == 0

    def test_single_item(self):
        assert knapsack([10], [4], 0) == 0
        assert knapsack([10], [4], 5) == 10
        assert knapsack([10], [4], 2) == 0
        assert knapsack([10], [4], 4) == 10

    def test_multiple_items(self):
        assert knapsack([1,4,5,7], [1,3,4,5], 7) == 9
        assert knapsack([1,4,5,7], [1,3,4,5], 6) == 8
        assert knapsack([2,7,3,9,6,10], [3,8,4,2,5,7], 10) == 19


if __name__ == '__main__':
    unittest.main()
