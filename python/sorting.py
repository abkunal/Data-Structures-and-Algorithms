""" Most popular comparison based sorting algorithms """
# Namely
# - Bubble Sort
# - Selection Sort
# - Insertion Sort
# - Quick Sort
# - Merge Sort

import unittest
import random
import time

# =============================================================================
# Bubble Sort
def bubble_sort(array):
    """ Sorts the given array using bubble sort technique """
    assert type(array) == list
    length = len(array)
    for i in range(length-1):
        for j in range(length-i-1):
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]
    return array
# =============================================================================


# =============================================================================
# Selection Sort
def selection_sort(array):
    """ Sorts the array using the selection sort """
    length = len(array)
    for i in range(length):
        smallest = i
        for j in range(i+1, length):
            if array[smallest] > array[j]:
                smallest = j
        array[smallest], array[i] = array[i], array[smallest]
    return array
# =============================================================================

# =============================================================================
# Insertion Sort
def insertion_sort(array):
    """ Sorts the array using insertion sort """
    for i in range(1, len(array)):
        elem = array[i]
        j = i-1
        while j >= 0 and array[j] > elem:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = elem

    return array
# =============================================================================

# =============================================================================
# Merge Sort
def merge(B, C):
    """ Merges two sorted lists A and B and output list C which is also sorted """
    D = []
    i = j = 0

    while i < len(B) and j < len(C):
        if B[i] < C[j]:
            D.append(B[i])
            i += 1
        else:
            D.append(C[j])
            j += 1

    D += B[i:]
    D += C[j:]

    return D

def merge_sort(A):
    """ Sorting using merge sort in O(n log n) time. """
    if len(A) <= 1:
        return A
    
    mid = len(A) // 2
    B = merge_sort(A[:mid])
    C = merge_sort(A[mid:])
    
    return merge(B, C)
# =============================================================================

# =============================================================================
# QuickSort
def partition(A, l, r):
    """ 
        Selects A[l] as the pivot element and puts it in a certain way such 
        that all the elements to left of pivot are < pivot and all the elements
        to the right of pivot are >= pivot.
    """
    p = A[l]        # pivot element
    j = l

    for i in range(l+1, r+1):
        if A[i] < p:
            j += 1
            A[j], A[i] = A[i], A[j]
    A[j], A[l] = p, A[j]

    return j

def quick_sort(A, l, r):
    """ Randomized quicksort with expected time of O(n log n) """
    if l >= r:
        return A
    
    # random swap to choose better pivot
    rd = random.randint(l, r)
    A[rd], A[l] = A[l], A[rd]

    m = partition(A, l, r)
    quick_sort(A, l, m)
    quick_sort(A, m+1, r)
    return A
# =============================================================================


class TestBubbleSort(unittest.TestCase):
    """ Test Cases for bubble sort """

    def test_empty_list(self):
        assert bubble_sort([]) == []

    def test_single_element(self):
        assert bubble_sort([60]) == [60]

    def test_10_elements(self):
        assert bubble_sort([9,8,7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7,8,9]
        assert bubble_sort([9876,6545,24543,234567876,2,78,76,52,34,5678]) == [2,34,52,76,78,5678,6545,9876,24543,234567876]

    def test_1000_elements(self):
        #for j in range(1000):
        a = [random.randint(-999999999999999999, 9999999999999999999) for i in range(1000)]
        assert bubble_sort(a) == sorted(a)

    #def test_10000_elements(self):
    #    for j in range(1000):
    #        a = [random.randint(-999999999999999999, 9999999999999999999) for i in range(10000)]
    #        assert bubble_sort(a) == sorted(a)


class TestSelectionSort(unittest.TestCase):
    """ Test Cases for selection sort """

    def test_empty_list(self):
        assert selection_sort([]) == []

    def test_one_element(self):
        assert selection_sort([5]) == [5]
        assert selection_sort([200000000000]) == [200000000000]

    def test_10_elements(self):
        assert selection_sort([9,8,7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7,8,9]
        assert selection_sort([9877,67,5,4356,43,32,45,67865,4,6]) == [4,5,6,32,43,45,67,4356,9877,67865]

    def test_1000_elements(self):
        #for j in range(1000):
        a = [random.randint(-99999999999999999, 99999999999999999) for i in range(1000)]
        assert selection_sort(a) == sorted(a)

    #def test_10000_elements(self):
    #    for j in range(1000):
    #        a = [random.randint(-999999999999999999, 9999999999999999999) for i in range(10000)]
    #        assert selection_sort(a) == sorted(a)


class TestInsertionSort(unittest.TestCase):
    """ Test Cases for insertion sort """

    def test_empty_list(self):
        assert insertion_sort([]) == []

    def test_one_element(self):
        assert insertion_sort([5]) == [5]
        assert insertion_sort([200000000000]) == [200000000000]

    def test_10_elements(self):
        assert insertion_sort([9,8,7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7,8,9]
        assert insertion_sort([9877,67,5,4356,43,32,45,67865,4,6]) == [4,5,6,32,43,45,67,4356,9877,67865]

    def test_1000_elements(self):
        #for j in range(1000):
        a = [random.randint(-99999999999999999, 99999999999999999) for i in range(1000)]
        assert insertion_sort(a) == sorted(a)

    #def test_10000_elements(self):
    #    for j in range(1000):
    #        a = [random.randint(-999999999999999999, 9999999999999999999) for i in range(10000)]
    #        assert insertion_sort(a) == sorted(a)
    

class TestMergeSort(unittest.TestCase):
    """ Test Cases for merge sort """

    def test_empty_list(self):
        assert merge_sort([]) == []

    def test_one_element(self):
        assert merge_sort([5]) == [5]
        assert merge_sort([200000000000]) == [200000000000]

    def test_10_elements(self):
        assert merge_sort([9,8,7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7,8,9]
        assert merge_sort([9877,67,5,4356,43,32,45,67865,4,6]) == [4,5,6,32,43,45,67,4356,9877,67865]

    def test_1000_elements(self):
        for j in range(1000):
            a = [random.randint(-99999999999999999, 99999999999999999) for i in range(1000)]
            assert merge_sort(a) == sorted(a)

    def test_10000_elements(self):
        for j in range(1000):
            a = [random.randint(-999999999999999999, 9999999999999999999) for i in range(10000)]
            assert merge_sort(a) == sorted(a)


class TestQuickSort(unittest.TestCase):
    """ Test Cases for quick sort """

    def test_empty_list(self):
        assert quick_sort([]) == []

    def test_one_element(self):
        assert quick_sort([5]) == [5]
        assert quick_sort([200000000000]) == [200000000000]

    def test_10_elements(self):
        assert quick_sort([9,8,7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7,8,9]
        assert quick_sort([9877,67,5,4356,43,32,45,67865,4,6]) == [4,5,6,32,43,45,67,4356,9877,67865]

    def test_1000_elements(self):
        for j in range(1000):
            a = [random.randint(-99999999999999999, 99999999999999999) for i in range(1000)]
            assert quick_sort(a) == sorted(a)

    def test_10000_elements(self):
        for j in range(1000):
            a = [random.randint(-999999999999999999, 9999999999999999999) for i in range(10000)]
            assert quick_sort(a) == sorted(a)
    

if __name__ == '__main__':
    unittest.main()
