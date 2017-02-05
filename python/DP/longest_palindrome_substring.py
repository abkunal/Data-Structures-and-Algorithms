""" Longest palindrome substring """

import unittest

def lps(string):
    """ Finds the longest palindrome substring in the given string. """

    P = []
    length = len(string)
    
    # Find all possible palindromes in string by expanding.
    for i in range(length):
        l = i-1
        r = i+1

        while l >= 0 and r < length:
            if string[l] == string[r]:
                l -= 1
                r += 1
            else: break

        P.append(([l+1, r-1], r-1-(l+1)+1))
        
        l = i
        r = i+1
        while l >= 0 and r < length:
            if string[l] == string[r]:
                l -= 1
                r += 1
            else:
                break

        P.append(([l+1,r-1], r-1-(l+1)+1))
    
    # find the longest palindrome substring
    maxi = ([0,0], 0)

    for data in P:
        if maxi[1] < data[1]:
            maxi = data

    print("Longest palindrome substring: ", string[maxi[0][0]:maxi[0][1]+1])
    return maxi


class TestLPS(unittest.TestCase):
    """ test cases for lps function """

    def test_empty_string(self):
        assert lps("") == ([0,0], 0)

    def test_single_char_string(self):
        assert lps("a") == ([0,0], 1)
        assert lps("z") == ([0,0], 1)

    def test_two_char_strings(self):
        assert lps("aa") == ([0,1], 2)
        assert lps("ab") == ([0,0], 1)
        assert lps("GH") == ([0,0], 1)
        assert lps("gg") == ([0,1], 2)

    def test_odd_length_palindromes(self):
        assert lps("level") == ([0,4], 5)
        assert lps("never") == ([1,3], 3)
        assert lps("nitin") == ([0,4], 5)
        assert lps("kunal") == ([0,0], 1)
        assert lps("lol") == ([0,2], 3)
        assert lps("asdfsgsaaabbbcbbbaaadfgdfbhdfdsg") == ([7,19], 13)
        assert lps("dsfsdfsaaabbgbbaa") == ([8,16], 9)
        assert lps("aalevelddnitinasfsani") == ([12, 20], 9)
    
    def test_even_length_palindromes(self):
        assert lps("abba") == ([0,3], 4)
        assert lps("llbbccccbbll") == ([0,11], 12)
        assert lps("asdasdkunallanuksaas") == ([6,15], 10)
        assert lps("differ") == ([2,3], 2)
        assert lps("asdasdaaaaabbbbbbbbaaaasdfsdfs") == ([7,22], 16)


if __name__ == '__main__':
    unittest.main()
