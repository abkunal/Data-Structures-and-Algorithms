""" LRU Cache Implementation in python """

import unittest
import random

class LRUCache:
    """ The Least Recently Used caching algorithm """

    def __init__(self, size):
        assert size > 0
        self._n = size
        self._cache = {}   # prototype: {key: [value, priority]}

    def get(self, key):
        """ Returns the value of the given key if the key exists, -1 otherwise """
        if key in self._cache:
           
           # decrement the priority of all the keys which have priority 
            # more than that of given key, by 1
            for k in self._cache:
                if self._cache[k][1] > self._cache[key][1]:
                    self._cache[k][1] -= 1
           
           # set the priority of recently accessed key to highest
            self._cache[key][1] = len(self._cache) - 1
            return self._cache[key][0]
        
        else:
            return -1

    def set(self, key, value):
        """ 
            Sets the value of key to given value if key already exists
            if key doesn't exists and memory has space left inserts the key
            else deletes the LRU value from the key and inserts the given key
        """
        # if key exists in the cache
        if key in self._cache:
            
            # update the priority of the keys
            for k in self._cache:
                if self._cache[k][1] > self._cache[key][1]:
                    self._cache[k][1] -= 1
            
            # set key to new value
            self._cache[key] = [value, len(self._cache)-1]
        
        elif len(self._cache) >= self._n:
            
            # find the LRU key and deletes it from the cache memory
            key_to_del = None
            for k in self._cache:
                if self._cache[k][1] == 0:
                    key_to_del = k
                    break
            del self._cache[k]
            
            # decrease priority of all keys by 1
            for k in self._cache: self._cache[k][1] -= 1

            self._cache[key] = [value, self._n-1]
        
        else:
            l = len(self._cache)
            self._cache[key] = [value, l]

        return True


class TestLRUCache(unittest.TestCase):
    """ Test Cases for LRUCache class """

    def test_size_of_one(self):
        l = LRUCache(1)

        assert l.get(10) == -1
        assert l.get(20) == -1
        l.set(20, 3)
        assert l.get(20) == 3
        assert l.get(10) == -1

        l.set(20, 345)
        assert l.get(20) == 345

        l.set(10, 123)
        assert l.get(20) == -1
        assert l.get(10) == 123

    def test_size_of_three(self):
        l = LRUCache(3)

        assert l.get(100) == -1
        l.set(1, 234)
        assert l.get(1) == 234
        l.set(2, 678)
        assert l.get(1) == 234
        assert l.get(2) == 678
        l.set(1, 2463)
        assert l.get(1) == 2463
        assert l.get(2) == 678
        l.set(3, 9865)
        assert l.get(1) == 2463
        assert l.get(2) == 678
        assert l.get(3) == 9865
        l.set(3, 7654)
        l.set(2, 6445)
        l.set(1, 89)
        assert l.get(1) == 89
        assert l.get(2) == 6445
        assert l.get(3) == 7654
        l.set(4, 575)
        assert l.get(1) == -1
        assert l.get(3) == 7654
        assert l.get(2) == 6445
        assert l.get(4) == 575
        l.set(56, 65342)
        assert l.get(3) == -1
        assert l.get(2) == 6445
        assert l.get(4) == 575
        assert l.get(56) == 65342


if __name__ == '__main__':
    unittest.main()
