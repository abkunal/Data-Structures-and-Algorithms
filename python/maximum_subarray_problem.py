""" Maximum subarray problem in python """

import unittest
import random

def bruteforce_algorithm(array):
    """ 
        Solves the maximum subarray problem by trying every possible subarray 
        Returns the maximum subarray. Runs in O(n^2) time
    """
    assert type(array) == list
    length = len(array)
    # if array is empty or contains only one element
    if length == 0:
        return (None, None, 0)
    elif length == 1:
        return (0,0,array[0])

    start = None
    stop = None
    max_sum = -200000000000
    
    # for each number in the array
    for i in range(length):
        so_far_sum = 0
        # calculate the sum of subarray starting from the ith number in array
        for j in range(i, length):
            so_far_sum += array[j]
            # if maximum sum is less than what we have found now, update
            if max_sum < so_far_sum:
                max_sum = so_far_sum
                start = i
                stop = j
    return (start, stop, max_sum)


## Divide and Conquer Algorithm
def find_max_cross_subarray(array, low, mid, high):
    """ 
        Finds the maximum subarray across the middle region in array
    """
    left_sum = -2000000000000
    so_far_sum = 0
    for i in range(mid, low-1, -1):
        so_far_sum += array[i]
        if left_sum < so_far_sum:
            left_sum = so_far_sum
            max_left = i

    right_sum = -20000000000000
    so_far_sum = 0
    for j in range(mid+1, high+1):
        so_far_sum += array[j]
        if right_sum < so_far_sum:
            right_sum = so_far_sum
            max_right = j
    return (max_left, max_right, left_sum + right_sum)


def find_max_subarray(array, low, high):
    """
        Finds the maximum subarray present in given array. Runs in O(nlogn) time.
        array: An array of numbers
        low: left index
        high: right index
        Returns the index range of maximum subarray along with maximum subarray.
    """
    if len(array) == 0:
        return (None, None, 0)
    if low == high:
        return (low, high, array[low])
    else:
        mid = (low + high) // 2

        (left_low, left_high, left_sum) = find_max_subarray(array, low, mid)
        (right_low, right_high, right_sum) = find_max_subarray(array, mid+1, high)
        (cross_low, cross_high, cross_sum) = find_max_cross_subarray(array, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        
        else:
            return (cross_low, cross_high, cross_sum)



def linear_time_algorithm(array):
    """ Finds the maximum subarray in a given array in O(n) time """
    assert type(array) == list
    length = len(array)
    if length == 0:
        return (None, None, 0)
    elif length == 1:
        return (0,0,array[0])

    start = 0
    stop = None
    maximum = -2000000000000
    sum_so_far = 0
    for i in range(length):
        sum_so_far += array[i]
        if sum_so_far < array[i]: 
            sum_so_far = array[i]
            start = i
        
        if maximum < sum_so_far:
            maximum = sum_so_far
            stop = i

    return start, stop, maximum

class TestBruteforceAlgorithm(unittest.TestCase):
    """ Test Cases for bruteforce_algorithm function """
    def test_empty_array(self):
        self.assertEqual(bruteforce_algorithm([]), (None, None, 0))

    def test_one_element_array(self):
        self.assertEqual(bruteforce_algorithm([20000]), (0,0,20000))

    def test_two_element_array(self):
        self.assertEqual(bruteforce_algorithm([1000, -2000]), (0,0,1000))

    def test_eight_element_array(self):
        self.assertEqual(bruteforce_algorithm([20,-10,30,40,-80,90,5,-4]), (0, 6, 95))

    def test_16_element_array(self):    
        self.assertEqual(bruteforce_algorithm([13,-3,-25,20,-3,-16,-23,18,20,
        -7,12,-5,-22,15,-4,7]), (7, 10, 43))

    def test_randomly_using_find_max_subarray(self):
        #for i in range(1000):
        array = [random.randint(-500000000, 500000000) for j in range(10000)]
        bruteforce_data = bruteforce_algorithm(array)
        find_max_data = find_max_subarray(array, 0, 9999)
        self.assertEqual(bruteforce_data, find_max_data)

    def test_randomly_using_linear_algo(self):
        array = [random.randint(-10000000000, 10000000000) for i in range(10000)]
        bruteforce_data = bruteforce_algorithm(array)
        linear_data = linear_time_algorithm(array)
        self.assertEqual(bruteforce_data, linear_data)


class TestFindMaxAlgorithm(unittest.TestCase):
    """ Test Cases for find_max_algorithm function """
    def test_empty_array(self):
        self.assertEqual(find_max_subarray([],0,0), (None, None, 0))

    def test_one_element_array(self):
        self.assertEqual(find_max_subarray([324234], 0, 0), (0,0,324234))

    def test_two_element_array(self):
        self.assertEqual(find_max_subarray([23423,-2342], 0, 1), (0,0,23423))
        self.assertEqual(find_max_subarray([234234, 32423], 0, 1), (0,1,266657))
        self.assertEqual(find_max_subarray([-3342,-23423], 0, 1), (0, 0, -3342))

    def test_eight_element_array(self):
        self.assertEqual(find_max_subarray([20,-10,30,40,-80,90,5,-4], 0, 7), (5, 6, 95))

    def test_16_element_array(self):
        self.assertEqual(find_max_subarray([13,-3,-25,20,-3,-16,-23,18,20,
        -7,12,-5,-22,15,-4,7], 0, 15), (7, 10, 43))

    def test_randomly_using_bruteforce(self):
        array = [random.randint(-100000000, 100000000) for i in range(10000)]
        find_max_data = find_max_subarray(array, 0, 9999)
        bruteforce_data = bruteforce_algorithm(array)
        self.assertEqual(find_max_data, bruteforce_data)

    def test_randomly_using_linear_algorithm(self):
        array = [random.randint(-10000000000, 10000000000) for i in range(10000)]
        find_max_data = find_max_subarray(array, 0, 9999)
        linear_data = linear_time_algorithm(array)
        self.assertEqual(find_max_data, linear_data)


class TestLinearAlgorithm(unittest.TestCase):
    """ Test Cases for linear_time_algorithm """
    def test_empty_array(self):
        self.assertEqual(linear_time_algorithm([]), (None, None, 0))

    def test_one_element_array(self):
        self.assertEqual(linear_time_algorithm([12312]), (0,0,12312))

    def test_two_element_algorithm(self):
        self.assertEqual(linear_time_algorithm([23423,-2342]), (0,0, 23423))
        self.assertEqual(linear_time_algorithm([-32423, -676]), (1,1,-676))
        self.assertEqual(linear_time_algorith,([547668,4657543]), (0, 1, 5205211))

    def test_eight_element_array(self):
        self.assertEqual(find_max_subarray([20,-10,30,40,-80,90,5,-4]), (5, 6, 95))

    def test_16_element_array(self):
        self.assertEqual(find_max_subarray([13,-3,-25,20,-3,-16,-23,18,20,
        -7,12,-5,-22,15,-4,7]), (7, 10, 43))



if __name__ == '__main__':
    unittest.main()
