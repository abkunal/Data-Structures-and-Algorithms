""" Sorting in Linear Time """

def Counting_Sort( array, k ):
	""" 
		Counting Sort is a linear time algorithm and works well
		when range of elements to be sorted is small.
		Assumes that elements are integers between 0 and k
		array: an array of n integers
		k: Maximum number present in the array
	"""
	n = len(array)
	# initialize helper list
	helper = [0 for i in range(k+1)]
	
	# find how many times an integer comes in the array
	for i in range( n ):
		helper[array[i]] += 1
	
	# find how many integers are less than equal to a particular integer
	for i in range( 1, k + 1 ):	
		helper[i] = helper[i] + helper[i-1]
	
	# initialize output array
	output = [0 for i in range(n)]
	
	# put integers at their appropriate position maintaining stability
	for i in range( n-1, -1, -1 ):
		output[helper[array[i]]-1] = array[i]
		helper[array[i]] -= 1
		
	return output
	
	
#arr = [2,5,3,0,2,3,0,3]
#print( Counting_Sort(arr, 5) )


def Counting_Sort_Digit( array, digit ):
	""" 
		Same as counting sort, but sorts elements by a particular digit.
		If digit is 1 then sorts by least significant, if digit equal to
		no of digits of an integer in array then sorts by least significant. 
	"""
	helper = [0 for i in range(10)]
	# convert integers into strings to easily sort by digit
	temp = list( map( str, array ) )
	for elem in temp:
		helper[int(elem[-digit])] += 1
	
	for i in range( 1, 10 ):
		helper[i] += helper[i-1]
	
	output = [0 for i in range(len(array))]
	for i in range(len(array) - 1, -1, -1 ):
		output[helper[int(temp[i][-digit])] -1] = array[i]
		helper[int(temp[i][-digit])] -= 1
	
	return output

#a = [i for i in range(9, -1, -1)]
#print( Counting_Sort_Digit( a, 1 ) )

def Radix_Sort( array, d ):
	""" 
		Sorts the integers in the array from least significant digit to
		the most significant digit. Integers are base 10.
		Assumes the elements in array are integers of d digits.
		array: a list of integers
		d: number of digits
	"""
	for i in range( 1, d + 1 ):
		array = Counting_Sort_Digit(array, i)
		print( array )
	
	return array

#a = [329, 457, 657,839,436,720,355]
#print( Radix_Sort(a, 3) )
	
def Bucket_Sort( array, k ):
	"""
		Sorts elements inside array by using k buckets
		array: an array/list of n elements (all integers, from 0 to k)
		k: Value of maximum integer present in the array
	"""
	n = len( array )
	buckets = [0 for i in range(k+1)]
	for i in range( n ):
		buckets[array[i]] += 1
		
	output = []
	for i in range( k + 1 ):
		for j in range( buckets[i] ):
			output.append(i)
			
	return output
