""" Implementation of a dynamic array in python """

import unittest
import random

class Array:
    
    def __init__(self):
        self._capacity = 5
        self._size = 0
        self._array = [None for i in range(5)]

    def size(self):
        return self._size

    def capacity(self):
        return self._capacity

    def is_empty(self):
        """ Return True if Array is empty, False otherwise """
        if self._size == 0:
            return True
        return False

    def at(self, index):
        """ Return the item at the given index """
        assert index < self._size and index >= 0
        return self._array[index]

    def push(self, item):
        """ Add the given item at the end of array """
        self.resize()
        if self._size < self._capacity:
            self._array[self._size] = item
            self._size += 1
            return True
        return False

    def insert(self, index, item):
        """ 
            Insert item at index, shifts that index's value and trailing 
            elements to the right.
        """
        assert index <= self._size 
        self.resize()
        if self._size < self._capacity:
            self._size += 1
            self.resize()
            for i in range(self._size, index, -1):
                self._array[i] = self._array[i-1]
            self._array[index] = item
            return True
        return False

    def prepend(self, item):
        """ Insert item at the start of the array """
        return self.insert(0, item)

    def pop(self):
        """ Remove an item from the end of array and returns it """
        self.resize()
        if self._size > 0:
            item = self._array[self._size-1]
            self._size -= 1
            return item
        return False

    def delete(self, index):
        """ Delete item at index, shifting all trailing elements left """
        assert index < self._size
        self.resize()
        if self._size > 0:
            item = self._array[index]
            for i in range(index, self._size):
                self._array[i] = self._array[i+1]
            self._size -= 1
            return True
        return False
    
    def find(self, item):
        """ Looks for value and returns first index with that value, -1 otherwise """
        for i in range(self._size):
            if self._array[i] == item:
                return i
        return -1

    def remove(self, item):
        """ Looks for value and removes index holding it, even in multiple places """
        if self._size == 0:
            return False
        
        self.resize()
        i = 0
        while True:
            if i >= self._size:
                break
            if self._array[i] == item:
                self.delete(i)
            else:
                i += 1
        return True

    def resize(self):
        """ 
            When array is full, doubles the capacity of the array
            When size of array is 1/4 of capacity, resize to half
        """
        if self._size == 0:
            self._capacity = 5
            self._array = [None for i in range(5)]
        elif self._size ==  self._capacity:
            # new capacity for the array
            new_capacity = int(self._capacity * 1.5) + 1
            new_array = [None for i in range(new_capacity)]
            # copy all the elements from the original array to resized array
            for i in range(self._size):
                new_array[i] = self._array[i]
            
            self._array = new_array
            self._capacity = new_capacity

        # if size is 1/4 of the capacity
        elif self._size <= int((1//4) * self._capacity):
            new_capacity = self._capacity // 2
            new_array = [None for i in range(new_capacity)]

            for i in range(self._size):
                new_array[i] = self._array[i]
            print("Half: ", new_array)
            self._array = new_array
            self._capacity  =new_capacity
        else:
            return True


class TestArray(unittest.TestCase):
    """ Test cases for Array class """
    def test_array(self):
        arr = Array()
        assert arr.pop() == False
        assert arr.is_empty() == True
        assert arr.size() == 0
        assert arr.find(200) == -1

        for i in range(10):
            assert arr.push(i) == True
        
        assert arr.find(5) == 5
        assert arr.at(9) == 9
        assert arr.size() == 10

        for i in range(9, -1, -1):
            assert arr.pop() == i

        assert arr.find(8) == -1
        assert arr.size() == 0
        
        for i in range(100, 200):
            assert arr.prepend(i) == True

        assert arr.at(50) == 149
        assert arr.at(99) == 100
        assert arr.size() == 100

        for i in range(99, -1, -1):
            assert arr.delete(i) == True

        assert arr.size() == 0

        for i in range(5000, 6000):
            assert arr.insert(0, i) == True

        assert arr.size() == 1000
        assert arr.find(5500) == 499
        assert arr.find(5000) == 999
        assert arr.find(5999) == 0
        assert arr.at(200) == 5799

        for i in range(5000, 6000):
            assert arr.remove(i) == True

        assert arr.size() == 0

    def test_using_python_list(self):
        arr = Array()
        lst = []

        # Enter 1000 numbers in the list and array
        for i in range(1000):
            arr.push(i)
            lst.append(i)
        
        assert arr.size() == len(lst)
        # check for equality
        for i in range(1000):
            assert arr.at(i) == lst[i]

        # Check pop()
        for i in range(1000):
            assert arr.pop() == lst.pop()

        assert arr.size() == len(lst)
        for i in range(10000):
            arr.push(i)
            lst.append(i)

        assert arr.size() == len(lst)
        for i in range(60000, 60030):
            arr.insert(500, i)
            lst.insert(500, i)

        for i in range(10030):
            assert arr.at(i) == lst[i]
        
        # Delete from an index
        for i in range(500, 700):
            arr.delete(i)
            lst.pop(i)
        
        for i in range(9830):
            assert arr.at(i) == lst[i]


        for i in range(100, 400):
            assert arr.find(i) == lst.index(i)

if __name__ == '__main__':
    unittest.main()
