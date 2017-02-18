""" Knuth-Morris-Pratt (KMP) Substring Search """

import unittest

def suffix_prefix_array(pattern):
    """
        Takes a string pattern and returns an array specifying position
        of same suffix and prefixes.
        pattern: A string
        Returns an array.
    """
    assert type(pattern) == str

    l = len(pattern)
    P = [0 for i in range(l)]

    i = 1
    while i < l:
        j = 0

        while j < i and i < l:
            if pattern[j] == pattern[i]:
                P[i] = j + 1
                j += 1
                i += 1
            elif j != 0:
                j = P[j-1]
            else:
                P[i] = 0
                break
        i += 1

    return P


def kmp_substring_search(text, pattern):
    """
        Takes two strings text and pattern and finds the location of first
        occurence of pattern in text if found, -1 otherwise.
        text: a string
        pattern: a string
        Returns an integer
    """

    P = suffix_prefix_array(pattern)
    end = 0

    i = 0
    j = 0
    while i < len(text) and j < len(pattern):
        j = 0
        
        while j < len(P):
            if text[i] == pattern[j]:
                i += 1
                j += 1
                end = i - 1
            elif j != 0:
                j = P[j-1]
            else:
                break

        i += 1

    if j == 0:
        return -1
    else:
        print("Location: ", end - len(pattern) + 1)
    return end - len(pattern) + 1
