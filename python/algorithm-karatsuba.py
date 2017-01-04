""" Implementation of Karatsuba Integer Multiplication Algorithm """

def karatsuba( a, b ):
	""" 
		a and b are two n digit integers.
		Returns the product of a and b using Karatsuba Divide and Conquer Algo.
	"""
	# Base Case for this Recursive Algorithm
	if a < 10 or a < 10:
		return a * b
		
	length = max( len(str(a)), len(str(b)) ) # calculate length of numbers
	half_length = length // 2
	
	raised_to_half = 10**half_length
	
	# divide numbers in two parts
	a1 = a // ( raised_to_half )
	a0 = a % ( raised_to_half )
	b1 = b // ( raised_to_half )
	b0 = b % ( raised_to_half )
	
	z2 = karatsuba( a1, b1 )
	z0 = karatsuba( a0, b0 )
	z1 = karatsuba( a1 + a0, b1 + b0 ) - z2 - z0
	
	return z2 * (10**(2*half_length)) + z1 * ( raised_to_half ) + z0
	
