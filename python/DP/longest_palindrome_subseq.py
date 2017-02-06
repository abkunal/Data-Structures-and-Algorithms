""" Longest Palindrome Subsequence using Dynamic Programming """

import unittest

def lps(s):
    """ 
        s is a string. Finds the length of the longest palindrome subsequence
        in the given string.
    """
    length = len(s)

    if length == 0:
        return 0

    L = [[0 for i in range(length)] for j in range(length)]

    for d in range(length):
        L[d][d] = 1

    for i in range(1, length+1):
        l = 0
        r = l + i

        while r < length:
            if s[l] == s[r]:
                L[l][r] = int(L[l+1][r-1]) + 2
            else:
                L[l][r] = max((L[l][r-1]), L[l+1][r])

            l += 1
            r += 1

    print("Length of LPS: ", L[0][length-1])
    
    return L[0][length-1]


class TestLPS(unittest.TestCase):
    """ Test cases for lps function """

    def test_empty_string(self):
        assert lps("") == 0

    def test_single_char(self):
        assert lps("a") == 1
        assert lps("k") == 1

    def test_two_chars(self):
        assert lps("aa") == 2
        assert lps("ab") == 1
        assert lps("gh") == 1
        assert lps("56") == 1
        assert lps("22") == 2

    def test_substring_palindromes(self):
        assert lps("nitin") == 5
        assert lps("Level") == 3
        assert lps("level") == 5
        assert lps("eve") == 3
        assert lps("titit") == 5
        assert lps("dsfsdfsameemas") == 8

    def test_uncontinuous_strings(self):
        assert lps("kauukaz") == 4
        assert lps("agbdba") == 5
        assert lps("dkjaklevelsdclevelshdkhdak") == 17


if __name__ == '__main__':
    unittest.main()
    
