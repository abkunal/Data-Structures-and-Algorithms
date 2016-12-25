""" Implementation of Queue Data Structure """

class Queue( object ):
	""" A Queue is a FIFO (First in, First Out) data structure. """
	
	def __init__( self ):
		self._storage = {}
		self._start = -1
		self._end = -1
		self._MAX = 20
		
	def enqueue( self, value ):
		""" Insert an item in the queue """
		if self._end >= self._MAX - 1:
			print( "Queue is Full!" )
			return False
			
		if self._start == -1:
			self._start += 1
		self._end += 1
		self._storage[self._end] = value
		return True
		
	def dequeue( self ):
		""" Delete an item from the start of the queue """
		if self._start == -1:
			print( "Queue is empty!" )
			return False
		
		item = self._storage[self._start]
		# When a single item is present in the queue
		if self._start == self._end:
			 del self._storage[self._start]
			 self._start = self._end = -1
			 return item
			 
		del self._storage[self._start]
		self._start += 1
		return item
			 
	def traverse( self ):
		""" Traverse and print the queue """
		
		if self._start == -1:
			print( "Queue is empty!" )
			return False
		
		print( "Queue: ", end="" )
		for i in range( self._start, self._end + 1 ):
			print( self._storage[i], end=" " )
		print( "" )
		
		return True
		
	def size( self ):
		""" Return the size of queue """
		if self._start == -1:
			return 0
		elif self._start == self._end:
			return 1
		else:
			return self._end - self._start + 1
			
			
class CircularQueue( Queue ):
	""" 
		A circular queue is a queue in which position of end doesn't decide
		whether queue is full or not
	"""
	
	def __init__( self ):
		super().__init__()
		
	def enqueue( self, value ):
		""" Insert an element at the end of queue. """
		if self.size() >= self._MAX:
			print( "Queue is full!" )
			return False
			
		# if queue is empty
		if self._start == -1:
			self._start += 1
		self._end = ( self._end + 1 ) % self._MAX
		self._storage[self._end] = value
		return True
		
	def dequeue( self ):
		""" Delete an item from the front of the stack """
		
		if self.size() == 0:
			print( "Queue is empty!" )
			return False
		
		item = self._storage[self._start]
		# queue contains only one element
		if self._start == self._end:
			del self._storage[self._start]
			self._start = self._end = -1
			return item
		
		del self._storage[self._start]
		self._start = ( self._start + 1 ) % self._MAX
		return item
	
	def traverse( self ):
		if self.size() == 0:
			print( "Queue is empty!" )
			return False
		print( "Queue: ", end="" )
		start = self._start
		while start != self._end:
			print( self._storage[start], end=" " )
			start = (start + 1) % self._MAX
		print( self._storage[self._end] )
		return True
		
	def size( self ):
		if self._start == -1:
			return 0
		elif self._start == self._end:
			return 1
		elif self._end > self._start:
			return self._end - self._start + 1
		else:
			return self._MAX - self._start + self._end + 1
			
			
class PriorityQueue( object ):
	""" 
		A priority queue is a queue in which elements are accessed according
		to their priorities.
	"""
	def __init__( self, levels ):
		self._levels = levels
		self._storage = {}
		
		for i in range( levels ):
			self._storage[i] = CircularQueue()
	
	def enqueue( self, value, level ):
		""" Inserts an item at a specified level """
		return self._storage[level].enqueue( value )
		
	def dequeue( self ):
		""" delete an item with the highest priority """
		for i in range( self._levels ):
			if ( self._storage[i].size() > 0 ):
				return self._storage[i].dequeue()
				
		return False
	
	def traverse( self ):
		""" Displays the content of the queue """
		if self.size() == 0:
			print( "Queue is empty!" )
			return False
	
		print( "Priority Queue: " )
		for i in range( self._levels ):
			if ( self._storage[i].size() > 0 ):
				print( "Level " + str(i) + ": " + str(self._storage[i].traverse()) )
			
		return True
	
	def size( self ):
		""" Returns the size of the priority queue """
		size = 0
		for i in range( self._levels ):
			size += self._storage[i].size()
			
		return size
