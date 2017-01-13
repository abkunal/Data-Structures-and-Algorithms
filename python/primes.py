""" Program to find prime numbers between 2 and n """

import unittest
import random
from math import sqrt


def find_primes(n):
	""" 
		n is a positive integer.
		Returns a list all the prime numbers between 2 and n, empty list otherwise
	"""
	assert n >= 0
	primes = [True for i in range(n+1)]
	if n >= 1:
		primes[0] = primes[1] = False
	else:
		primes[0] = False

	for i in range(2, int(sqrt(n)+1)):
		for j in range(2*i, n+1, i):
			primes[j] = False
	output = [i for i in range(n+1) if primes[i] == True]
	return output


def is_prime(n):
	""" Returns True if n is prime, False otherwise """
	assert n >= 0
	prime = True
	
	if n <= 1: return False

	for i in range(2, int(sqrt(n)+1)):
		if n % i == 0:
			prime = False
			break
	return prime


class TestIsPrime(unittest.TestCase):
	""" Test cases for is_prime function """
	def test_n_equals_0(self):
		self.assertFalse(is_prime(0))

	def test_n_equals_1(self):
		self.assertFalse(is_prime(1))

	def test_n_equals_2(self):
		self.assertTrue(is_prime(2))

	def test_n_equals_3(self):
		self.assertTrue(is_prime(3))

	def test_n_equals_10(self):
		self.assertFalse(is_prime(10))

	def test_n_equals_97(self):
		self.assertTrue(is_prime(97))


class TestFindPrimes(unittest.TestCase):
	""" Test cases for find_primes function """
	def test_n_equals_0(self):
		self.assertEqual(find_primes(0), [])
	
	def test_n_equals_1(self):
		self.assertEqual(find_primes(1), [])

	def test_n_equals_2(self):
		self.assertEqual(find_primes(2), [2])
	
	def test_n_equals_10(self):
		self.assertEqual(find_primes(10), [2,3,5,7])

	def test_n_equals_50(self):
		self.assertEqual(find_primes(50), [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47])

	def test_using_is_prime(self):
		first_primes = find_primes(100000)
		second_primes = []
		for i in range(2, 100001):
			if is_prime(i):
				second_primes.append(i)
		self.assertTrue(first_primes == second_primes)

if __name__ == '__main__':
	unittest.main()
