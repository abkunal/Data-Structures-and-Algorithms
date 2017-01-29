""" Longest Common Subsequence problem using Dynamic Programming """

import unittest


def lis(A):
    """
        A: a list of integers
        Find the longest increasing subsequence in A.
        Returns a tuple (start,end), start -> starting index, b -> ending index
    """
    # Trivial case
    if len(A) == 0:
        return None
    if len(A) == 1:
        return (0,0)
    start = end = 0
    arr = []
    
    # Find all the increasing subsequences in A
    for i in range(1, len(A)):
        if A[i] < A[i-1]:
            arr.append((start, end))
            start = end = i
        else:
            end += 1
    arr.append((start, end))
    
    # Find the longest increasing subsequence
    lis = None
    for t in arr:
        if lis is None or (lis[1] - lis[0]) < (t[1] - t[0]):
            lis = t

    return lis


class Testlis(unittest.TestCase):
    """ Test Cases for longest increasing subsequence """

    def test_empty_array(self):
        self.assertEqual(lis([]), None)

    def test_one_element_array(self):
        self.assertEqual(lis([20]), (0,0))

    def test_two_element_array(self):
        self.assertEqual(lis([10, 20]), (0, 1))
        self.assertEqual(lis([10, 10]), (0, 1))
        self.assertEqual(lis([3000, 1000]), (0, 0))
        
    def test_multiple_elems(self):
        self.assertEqual(lis([9,8,7,6,5,4,3,2,1,0]), (0,0))
        self.assertEqual(lis([0,1,2,3,4,5,6,7,8,9]), (0, 9))
        self.assertEqual(lis([234,2464,778709876,5,434,23,4252]), (0, 2))
        self.assertEqual(lis([100, 2,4,5,6,7, 10000, 10000000, 99999999, 454,]), (1, 8))
        self.assertEqual(lis([343, 45, 50, 200, 100, 120, 160, 300]), (4,7))
        self.assertEqual(lis([200,23,56,300, 27, 45, 67, 78, 90, 10086, 35433, 2000]), (4, 10))


if __name__ == '__main__':
    unittest.main()
