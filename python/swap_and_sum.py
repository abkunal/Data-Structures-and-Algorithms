""" Find a pair of elements swapping which makes sum of two arrays same """

def get_target(A, B):
	sumA = sum(A)
	sumB = sum(B)

	if (sumA - sumB) % 2 != 0:
		return 0
	else:
		return (sumA - sumB) / 2

def find_swap_values(A, B):
	# sort the two arrays
	A.sort()
	B.sort()

	target = get_target(A, B)

	# answer not possible
	if target == 0:
		return -1 
	
	i, j = (0,0)
	while i < len(A) and j < len(B):
		diff = A[i] - B[j]

		# if diff equals target, swap values found
		if diff == target:
			return (A[i], B[j])
		# diff < target, Increase count of A
		elif diff < target:
			i += 1
		# diff > target, increase count of B
		else:
			j += 1

A = [4, 1, 2, 1, 1, 2]
B = [ 1, 6, 3, 3 ]

print(find_swap_values(A, B))