""" Algorithms and programs solving problems using Dynamic Programming """

## Fibonacci Numbers
def naive_fib(n):
	""" The naive recursive algorithm to compute nth fibonacci number. """
	assert n >= 1
	if n <= 2:
		return 1
	else:
		return naive_fib(n-1) + naive_fib(n-2)

memo = {}
def memoized_fib(n):
	""" Using memoization to compute nth fibonacci number in linear time O(n). """
	assert n >= 1
	if n in memo:
		return memo[n]
	if n <= 2:
		fib = 1
	else:
		fib = memoized_fib(n-1) + memoized_fib(n-2)
	memo[n] = fib
	return fib

def iterative_fib(n):
	""" Iteratively compute nth fibonacci number using bottom-up approach """
	assert n >= 1
	fib = {}
	for i in range(1, n+1):
		if i <= 2:
			f = 1
		else:
			f = fib[i-1] + fib[i-2]
		fib[i] = f
	return fib[n]

## Test Cases for fibonacci

import unittest
class TestNaiveFibonacci(unittest.TestCase):
	""" Test Cases for naive_fib function """
	def test_one(self):
		self.assertEqual(naive_fib(1), 1)
	
	def test_two(self):
		self.assertEqual(naive_fib(2), 1)

	def test_five(self):
		self.assertEqual(naive_fib(5), 5)

	def test_ten(self):
		self.assertEqual(naive_fib(10), 55)

class TestMemoizedFib(unittest.TestCase):
	""" Test Cases for memoized_fib function """
	def test_one(self):	
		self.assertEqual(memoized_fib(1), 1)

	def test_two(self):
		self.assertEqual(memoized_fib(2), 1)
	                
	def test_five(self):
		self.assertEqual(memoized_fib(5), 5)

	def test_ten(self):
		self.assertEqual(memoized_fib(10), 55)

	def test_thirty(self):
		self.assertEqual(memoized_fib(30), 832040)
	

class TestIterativeFib(unittest.TestCase):
	""" Test cases for iterative_fib function """
	def test_one(self):
		self.assertEqual(iterative_fib(1), 1)

	def test_two(self):
		self.assertEqual(iterative_fib(2), 1)

	def test_five(self):
		self.assertEqual(iterative_fib(5), 5)

	def test_ten(self):
		self.assertEqual(iterative_fib(10), 55)

	def test_fifteen(self):
		self.assertEqual(iterative_fib(15), 610)

	def test_thirty(self):
		self.assertEqual(iterative_fib(30), 832040)
	
	def test_fourty(self):
		self.assertEqual(iterative_fib(40), 102334155)

if __name__ == '__main__':
	unittest.main()
