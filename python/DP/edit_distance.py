""" Minimum Edit Distance by Dynamic Programming """

from sys import maxsize
import unittest

def edit_distance(s1, s2):
    """
        s1 and s2 are two strings.
        Calculates the minimum number of edits to convert s2 into s1.
    """
    assert type(s1) == str and type(s2) == str
    
    l1 = len(s1)
    l2 = len(s2)
    
    if l1 == 0 and l2 == 0:
        return 0

    E = [[maxsize for i in range(l2+1)] for j in range(l1+1)]
    direc = [["" for i in range(l2+1)] for j in range(l1+1)]

    # Handle cases for null string conversion
    for i in range(l2+1):
        E[0][i] = i

    for j in range(l1+1):
        E[j][0] = j
    

    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if s1[i-1] == s2[j-1]:
                E[i][j] = E[i-1][j-1]
            else:
                E[i][j] = min(E[i-1][j], E[i-1][j-1], E[i][j-1]) + 1
    
    print_edits(E, s1, s2)
    print("Minimum Edit Distance: ", E[l1][l2])
    return E[l1][l2]


def print_edits(E, s1, s2):
    """ Print the actual edits that needs to be done. """
    i = len(E)-1
    j = len(E[0])-1

    while True:
        
        if i == 0 or j == 0:
            break
        elif s1[i-1] == s2[j-1]:
            i -= 1
            j -= 1

        elif E[i][j] == E[i-1][j-1] +1:
            print("Replace ", s2[j-1], " in 2nd with ", s1[i-1], " in 1st")
            i -= 1
            j -= 1

        elif E[i][j] == E[i-1][j] + 1:
            print("Delete from first string: ", s1[i-1])
            i -= 1

        elif E[i][j] == E[i][j-1] + 1:
            print("Delete from second string: ", s2[j-1])
            j -= 1
        
        else:
            raise Exception("Something's wrong!")


class TestEditDistance(unittest.TestCase):
    """ Tests for edit_distance function """
    
    def test_empty_to_empty(self):
        assert edit_distance("", "") == 0

    def test_string_to_empty(self):
        assert edit_distance("", "kunal") == 5
        assert edit_distance("", "a") == 1
        assert edit_distance("", "This is a string") == 16

    def test_empty_to_string(self):
        assert edit_distance("kunal", "") == 5
        assert edit_distance("abcdef", "") == 6
        assert edit_distance("a", "") == 1
        assert edit_distance("This is an example string", "") == 25

    def test_same_to_same(self):
        assert edit_distance("kunal", "kunal") == 0
        assert edit_distance("a", "a") == 0
        assert edit_distance("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz") == 0
        assert edit_distance("same string!", "same string!") == 0

    def test_same_length_strings(self):
        assert edit_distance("kunal", "yadav") == 4
        assert edit_distance("github", "gitnop") == 3
        assert edit_distance("asdfghjkl", "asdlkjfgh") == 6
        assert edit_distance("one string", "two string") == 3

    def test_different_length_string(self):
        assert edit_distance("same", "different") == 8
        assert edit_distance("easy to?", "hard!") == 7
        assert edit_distance("its getting", "Complicated!") == 11
        assert edit_distance("it may be", "enough, is it?") == 13
        assert edit_distance("something", "someone") == 4
        assert edit_distance("looks like last time", "looks in here bit") == 10


if __name__ == '__main__':
    unittest.main()
