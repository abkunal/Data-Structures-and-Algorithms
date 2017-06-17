""" Huffman coding implementation """

import unittest
import heapq

class Node:
	""" A node of a tree """

	def __init__(self, name, val, left=None, right=None):
		self._left = left
		self._right = right
		self._name = name
		self._val = val

	def get_name(self):
		return self._name

	def get_val(self):
		return self.val

	def get_left_child(self):
		return self._left

	def get_right_child(self):
		return self._right

	def __lt__(self, other):
		return self._name < other._name


def prefix_traverse(n, codes, string=""):
	""" Generates the huffman code of the charaters using the given node 
		Each time while traversing, when we go to a left node we add "0"
		and when we go to right node we add "1".

		n: Node
		codes: dictionary {charater: code}
		string: code
	"""
	if n is not None:
		prefix_traverse(n.get_left_child(), codes, string+"0")
		if n.get_name() != "i":
			codes[n.get_name()] = string
		prefix_traverse(n.get_right_child(), codes, string+"1")


def huffman_coding(data):
	""" Returns the generated huffman code of given characters using their
		frequencies.

		data: dictionary {character: frequency}
	"""
	assert type(data) == dict

	if data == {}:
		return {}

	# Initializing external nodes from data
	h = [(data[key], Node(key, data[key])) for key in data]
	heapq.heapify(h)

	# At the end of the loop there will be a single node present in the minheap
	for i in range(len(data)-1):
		# Pop out two smallest nodes
		x = heapq.heappop(h)
		y = heapq.heappop(h)

		# Create a new node and add "x" as its left child and "y" as its right
		z = Node("i", x[0] + y[0], x[1], y[1])

		# Push this new node into the heap
		heapq.heappush(h, (x[0]+y[0], z))

	# Generate codes for characters by using preorder traversal
	t = heapq.heappop(h)
	codes = {}
	prefix_traverse(t[1], codes)
	return codes


#data = {"a": 5, "b":9, "c": 12, "d":13, "e": 16, "f": 45}
#test = huffman_coding(data)

class TestHuffmanCoding(unittest.TestCase):
	""" Test Cases for huffman_coding function """

	def test_empty_input(self):
		data = {}
		codes = huffman_coding(data)
		assert codes == {}

	def test_single_input(self):
		data = {"a": 10}
		codes = huffman_coding(data)
		assert codes == {"a": ""}

	def test_two_inputs(self):
		data = {"a": 10, "b": 30}
		codes = huffman_coding(data)
		assert codes == {"a": "0", "b": "1"}

	def test_multiple_inputs1(self):
		data = {"a": 5, "b":9, "c": 12, "d":13, "e": 16, "f": 45}
		codes = huffman_coding(data)
		assert codes == {"a":"1100", "b":"1101", "c":"100", "d":"101", 
						"e":"111", "f":"0"}

	def test_multiple_inputs2(self):
		data = {"a":5, "b":5, "c":5, "d":5, "e":5, "f":5}
		codes = huffman_coding(data)
		assert codes == {'e': '00', 'f': '01', 'c': '100', 'd': '101', 
						'a': '110', 'b': '111'}


if __name__ == '__main__':
	unittest.main()