""" Find common elements in 3 sorted arrays """

import unittest

def common_elements(a1, a2, a3):
	i, j, k = (0, 0, 0)

	common = []
	while i < len(a1) and j < len(a2) and k < len(a3):
		if a1[i] == a2[j] and a2[j] == a3[k]:
			x =a1[i]
			common.append(x)
			i += 1
			j += 1
			k += 1
		elif a1[i] < a2[j]:
			i += 1
		elif a2[j] < a3[k]:
			j += 1
		else:
			k += 1

	return common


class TestCommonElements(unittest.TestCase):
	""" Test cases for function common_elements """

	def test_empty_arrays(self):
		assert common_elements([],[],[]) == []

	def test_partial_empty1(self):
		assert common_elements([],[],[1,2]) == []

	def test_partial_empty2(self):
		assert common_elements([],[4,5],[]) == []

	def test_partial_empty3(self):
		assert common_elements([3,5],[],[]) == []

	def test_partial_empty4(self):
		assert common_elements([4,6],[5,7],[]) == []

	def test_partial_empty5(self):
		assert common_elements([],[],[1,2]) == []

	def test_partial_empty6(self):
		assert common_elements([7,9],[],[1,2]) == []

	def test_partial_empty7(self):
		assert common_elements([],[5,8],[3,5]) == []

	def test_no_common1(self):
		assert common_elements([1,2,3], [4,5,6], [7,8,9]) == []

	def test_no_common2(self):
		assert common_elements([1,2], [1,3], [3,7]) == []

	def test_no_common3(self):
		assert common_elements([1], [1], [5]) == []

	def test_one_common(self):
		assert common_elements([1,2,3], [2,4,5], [2,8,9]) == [2]

	def test_two_common1(self):
		assert common_elements([1,2,3], [1,3,6,7], [1,2,3,5,7]) == [1,3]

	def test_two_common2(self):
		a1 = [1, 5, 10, 20, 40, 80]
		a2 = [6, 7, 20, 80, 100]
		a3 = [3, 4, 15, 20, 30, 70, 80, 120]
		assert common_elements(a1, a2, a3) == [20, 80]


if __name__ == '__main__':
	unittest.main()