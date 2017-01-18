""" Storing contacts of a phonebook using hashtable (Separate chaining). """

import unittest


class Node:
    """ A node contains information about a single person """
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    """ A singly linked list to provide chaining for the hashtable """

    def __init__(self):
        self._head = None
        self._size = 0

    def size(self):
        return self._size

    def push_front(self, key, value):
        """ Adds an item at the start of a list """
        node = Node(key, value)
        node.next = self._head
        self._head = node
        self._size += 1
        return True

    def search(self, key):
        """ Searches for a given key in the table """
        start = self._head

        while start is not None:
            if start.key == key:
                return start.value
            start = start.next

        return False

    def delete(self, key):
        """ If given key exists in the list, deletes it """
        current = previous =  self._head

        # list contains only a single node
        if self._size == 1:
            if current.key == key:
                self._head = None
                self._size -= 1
                return True
            else: return False
            
        while current is not None:
            if current.key == key:
                previous.next = current.next
                self._size -= 1
                return True

            previous = current
            current = current.next

        return False


class Phonebook:
    """ Phonebook to store contacts using hashtables """

    def __init__(self):
        self._names = []        # stores the names of the people
        self._numbers = []      # stores the mobile numbers of the people
        self._MAX = 10

        for i in range(self._MAX):
            self._names.append(LinkedList())
            self._numbers.append(LinkedList())

    def hash_name(self, name):
        """ Computes the hashed value of name """
        assert type(name) == str
        hashed = int(''.join([str(ord(c)) for c in name]))
        bucket = hashed % self._MAX
        return bucket

    def hash_number(self, number):
        """ Computes the hashed value of number """
        assert type(number) == int
        return number % self._MAX
        
    def add_contact(self, name, number):
        """ Adds a contact in the phonebook """
        hname = self.hash_name(name)
        hnumber = self.hash_number(number)

        self._names[hname].push_front(name, number)
        self._numbers[hnumber].push_front(number, name)

        return True

    def search_by_name(self, name):
        """ Searches a contact by name in the phonebook """
        hname = self.hash_name(name)
        return self._names[hname].search(name)

    def search_by_number(self, number):
        """ Searches a contact by number in the phonebook  """
        hnumber = self.hash_number(number)
        return self._numbers[hnumber].search(number)

    def delete_contact(self, name, number):
        """ Delete a contact from the phonebook """
        hname = self.hash_name(name)
        hnumber = self.hash_number(number)

        return self._names[hname].delete(name) and self._numbers[hnumber].delete(number)


class TestLinkedList(unittest.TestCase):
    """ Test Cases for LinkedList class """

    def test_simple_case(self):
        l = LinkedList()
        l.push_front('a', 20)
        assert l.size() == 1
        assert l.search('a') == 20

        l.push_front('b', 500)
        assert l.size() == 2

        assert l.search('b') == 500
        assert l.search('a') == 20

        assert l.delete('a') == True
        assert l.size() == 1
        assert l.search('a') == False

        assert l.delete('b') == True
        assert l.size() == 0
        print(l.search('b'))
        assert l.search('b') == False

    def test_hundred_input(self):
        l = LinkedList()

        for i in range(100):
            l.push_front(i, i)

        assert l.size() == 100
        assert l.search(1) == 1
        assert l.search(100) == False

        for i in range(50):
            assert l.delete(i) == True

        assert l.size() == 50
        assert l.search(1) == False
        assert l.search(50) == 50

        for i in range(50, 100):
            assert l.delete(i) == True

        assert l.size() == 0


class TestPhonebook(unittest.TestCase):
    """ Test Cases for phonebook """

    def test_two_names(self):
        p = Phonebook()
        p.add_contact('kunal', 123456789)

        assert p.search_by_name('kunal') == 123456789
        assert p.search_by_number(123456789) == 'kunal'

        p.add_contact('mark', 987654321)
        
        assert p.search_by_name('mark') == 987654321
        assert p.search_by_number(987654321) == 'mark'

        assert p.delete_contact('kunal', 123456789) == True
        assert p.search_by_name('kunal') == False
        assert p.search_by_number(123456789) == False

        assert p.delete_contact('mark', 987654321) == True
        assert p.search_by_name('mark') == False
        assert p.search_by_number(987654321) == False


if __name__ == '__main__':
    unittest.main()
