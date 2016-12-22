""" Peak Finder Algorithm """

""" One Dimensional Version """

# Naive Algorithm
def simple_peak_finder( array ):
	""" Finds a peak in the given array. """
	index = 0
	length = len( array )
	
	# if array is empty
	if length == 0:
		return -1
	# if array contains exactly one element
	elif length == 1:
		return 0
	elif length <= 2:
		if array[0] > array[1]:
			return 0
		else:
			return 1
	
	# search for peak in the middle of the list
	for i in range( 1, length - 1 ):
		if array[i] >= array[i-1] and array[i] >= array[i+1]:
			return i
	
	if array[length-1] >= array[length - 2]:
		return length-1
		

# Divide and Conquer Algorithm
def efficient_peak_finder( array, low, high ):
	""" 
		Divide and Conquer based peak finder algorithm.
		finds a peak value recursively by breaking the list into 2 halves
	"""
	length = len( array )
	# if array is empty
	if length == 0:
		return -1
	
	mid = int ( ( low + high ) / 2 )
	
	# if middle element is the first element in the list or last element or
	# middle element if greater than its left and right element 
	if ( mid == 0 or array[mid] >= array[mid-1] ) and ( mid == length - 1 or array[mid] >= array[mid+1] ):
		return mid
	
	# if middle element is less than its left element, search the left part
	# mid > 0 => condition when mid = 0, length = 2 and array[1] > array[0]
	elif mid > 0 and array[mid] < array[mid-1]:
		return efficient_peak_finder( array, low, mid-1 )
	
	# if middle element is less than its right element, search the right part 	
	else:
		return efficient_peak_finder( array, mid+1, high )

		
import unittest
#class TestSimplePeakFinder( unittest.TestCase ):
#	
#	def test_empty_array( self ):
#		a = []
#		self.assertEqual( simple_peak_finder( a ), -1 )
#		
#	def test_one_element( self ):
#		a = [2]
#		self.assertEqual( simple_peak_finder( a ), 0 )
#		
#	def test_two_elements( self ):
#		a = [1,2]
#		self.assertEqual( simple_peak_finder( a ), 1 )
#		a = [2,1]
#		self.assertEqual( simple_peak_finder( a ), 0 )
#		
#	def test_sorted_list( self ):
#		a = [1,2,3,5,6,7,9]
#		self.assertEqual( simple_peak_finder( a ), 6 )
#		
#	def test_unsorted_list( self ):
#		a = [10,40,50,60,20,80,100,15]
#		self.assertEqual( simple_peak_finder( a ), 3 )


# Tests for "efficient_peak_finder" function
class TestEfficientPeakFinder( unittest.TestCase ):
	
	def test_empty_array( self ):
		a = []
		self.assertEqual( efficient_peak_finder( a, 0, 0 ), -1 )
		
	def test_one_element( self ):
		a = [2]
		self.assertEqual( efficient_peak_finder( a, 0, 0 ), 0 )
		
	def test_two_elements( self ):
		a = [1,2]
		self.assertEqual( efficient_peak_finder( a, 0, 1 ), 1 )
		a = [2,1]
		self.assertEqual( efficient_peak_finder( a, 0, 1 ), 0 )
		
	def test_sorted_list( self ):
		a = [1,2,3,5,6,7,9]
		self.assertEqual( efficient_peak_finder( a, 0, 6 ), 6 )
		
	def test_unsorted_list( self ):
		a = [10,40,50,60,20,80,100,15]
		self.assertEqual( efficient_peak_finder( a, 0, 7 ), 3 )

		
if __name__ == '__main__':
	unittest.main()
