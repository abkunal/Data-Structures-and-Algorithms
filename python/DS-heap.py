""" Implementation of Heap and Heap Sort """

"""
	A heap is represented as a nearly complete binary tree.
	We will use array representation for the heap.
	
	Let A[1...n] be an array.
	Root of tree = first element ( i = 1 )
	Parent( i ) = i / 2
	Left( i ) = 2 * i
	Right( i ) = 2 * i + 1 
"""

""" MAX-HEAP """
infinity = -100000000
# Just a heap, not a max-heap nor a min-heap
heap = [infinity, 16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
heap_size = 10


def Parent( i ):
	""" Returns the index of the parent of node at heap[i] """
	return int( i / 2 )
	
def Left( i ):
	""" Returns the index of the left child of node at heap[i] """
	return int( 2 * i )
	
def Right( i ):
	""" Returns the index of the right child of node at heap[i] """
	return int( 2 * i + 1 )
	

def Max_Heapify( array, heap_size, i ):
	""" 
		Assumes that the trees rooted left(i) and right(i) are max-heaps
		Corrects a single violation of heap property in a subtree.
	"""
	left = Left( i )
	right = Right( i )
	largest = i
	# if left is the index of array and left child of i greater than i
	if left <= heap_size and array[left] > array[i]:
		largest = left
	# if right is the index of array and i's right child is > A[largest]
	if right <= heap_size and array[right] > array[largest]:
		largest = right
	# if either left or right child of i is greater than i, correct and proceed
	if largest != i:
		array[i], array[largest] = array[largest], array[i]
		Max_Heapify( array, heap_size, largest )
		
def build_max_heap( array ):	
	""" Builds a max-heap out of an unsorted array / heap """
	heap_size = len( array ) - 1
	for i in range( int( heap_size / 2 ), 0, -1 ):
		Max_Heapify( array, heap_size, i )
		
#print( "Just a heap: ", heap[1:] )
#build_max_heap( heap )
#print( "Max-heap: ", heap[1:] )

def Heap_Sort( A ):
	""" Sorts the array represented as heap """
	build_max_heap( A )
	heap_size = len( A ) - 1
	for i in range( len(A) - 1, 1, -1 ):
		A[1], A[heap_size] = A[heap_size], A[1]
		heap_size -= 1
		Max_Heapify( A, heap_size, 1 )
	return A
	
#Heap_Sort(heap)


""" MIN-HEAP """
def Min_Heapify( array, heap_size, i ):
	""" 
		Assumes that th trees rooted left(i) and right(i) are min-heaps
		Corrects a single violation of heap property in a subtree
	"""
	left = Left( i )
	right = Right( i )
	smallest = i
	if left <= heap_size and array[left] < array[i]:
		smallest = left
	if right <= heap_size and array[right] < array[smallest]:
		smallest = right
	if smallest != i:
		array[i], array[smallest] = array[smallest], array[i]
		Min_Heapify( array, heap_size, smallest )
		
def build_min_heap( array ):
	""" Builds a min-heap out of an unsorted array / heap """
	heap_size = len( array ) - 1
	for i in range( int( heap_size / 2 ), 0, -1 ):
		Min_Heapify( array, heap_size, i )

#build_min_heap( heap )

""" Priority Queues using Heaps """
"""
	4 operations will be performed
	HEAP-MAXIMUM: find the maximum element in the max-heap
	HEAP-EXTRACT-MAX: find and deletes the maximum element from the max-heap
	HEAP-INCREASE-KEY:	increases the key value of a particular element
	MAX-HEAP-INSERT: inserts a key into the max-heap
"""

def Heap_Maximum( array, heap_size ):
	if heap_size < 1:
		print( "Underflow!" )
		return False
	return array[1]
	
def Heap_Extract_Max( array, heap_size ):
	""" Extracts out the maximum element out of the array """
	if heap_size < 1:
		print( "Underflow!" )
		return False
	maximum = array[1]
	array[1], array[heap_size] = array[heap_size], array[1]
	heap_size = heap_size - 1
	Max_Heapify( array, heap_size, 1 )
	return maximum
	
def Heap_Increase_Key( array, i, key ):
	""" Increases the key value of a particular element """
	if key < array[i]:
		print( "new key is smaller than current key" )
		return False
	array[i] = key
	while i > 1 and array[Parent(i)] < array[i]:
		array[i], array[Parent(i)] = array[Parent(i)], array[i]
		i = Parent(i)
		
def Heap_Insert_Key( array, heap_size, key ):
	""" Inserts the given key into the heap """
	heap_size += 1
	array.append( -200000000000 )
	Heap_Increase_Key( array, heap_size, key )
	
print( Heap_Maximum() )
