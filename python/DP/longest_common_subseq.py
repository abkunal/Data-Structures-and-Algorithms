""" Longest Common subsequence(LCS) using Dynamic Programming """

import unittest

def lcs(s1, s2):
    """
        s1 and s2 are two strings.
        Finds the longest common subsequence of s1 and s2
    """
    assert type(s1) == str and type(s2) == str

    l1 = len(s1)
    l2 = len(s2)
    
    # when both strings are empty
    if l1 == 0 and l2 == 0:
        return 0

    L = [[0 for i in range(l2+1)] for j in range(l1+1)]
    
    # Trivial cases
    for i in range(l2+1):
        L[0][i] = 0

    for j in range(l1+1):
        L[j][0] = 0

    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if s1[i-1] == s2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    
    print_seq(L, s1, s2)
    print("Length of LCS: ", L[l1][l2])
    return L[l1][l2]


def print_seq(L, s1, s2):
    """ Prints the longest common subsequence """
    lcs = ""

    i = len(L) - 1
    j = len(L[0]) - 1

    while True:
        if i == 0 or j == 0:
            break
        elif s1[i-1] == s2[j-1]:
            lcs = s1[i-1] + lcs
            i -= 1
            j -= 1
        elif L[i][j-1] > L[i-1][j]:
            j -= 1
        else:
            i -= 1
    print(lcs)


class TestLongestCommonSubsequence(unittest.TestCase):
    """ Test Cases lcs function """

    def test_both_empty_string(self):
        assert lcs("", "") == 0
    
    def test_one_empty_string(self):
        assert lcs("", "hello") == 0
        assert lcs("hello", "") == 0
        assert lcs("some string", "") == 0

    def test_some_strings(self):
        assert lcs("a", "b") == 0
        assert lcs("hello", "Hello") == 4
        assert lcs("hello, world", "hello, World") == 11
        assert lcs("abababab", "babababa") == 7
        assert lcs("longest common subsequence", "longest palindrome subsequence") == 22


if __name__ == '__main__':
    unittest.main()
