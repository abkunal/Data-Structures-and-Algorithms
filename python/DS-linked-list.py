""" Implementation of linked list """

class Node( object ):
	""" A Node for singly linked list """

	def __init__( self, item ):
		self.value = item
		self.next = None


class LinkedList( object ):
	""" A linked list """

	def __init__( self ):
		""" Initialize the list """
		self.head = None
		self.tail = None
		self.length = 0

	def traverse( self ):
		""" print out the contents of the list """
		if self.head is None:
			print( "List is empty!" )
			return False

		print ( "List: ", end="" )
		current = self.head
		while current is not None:
			print( current.value, end=" " )
			current = current.next
		print()


	def insert_at_beginning( self, value ):
		""" Insert a node at the beginning of the list """
		node = Node( value )

		# if list is empty
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			node.next = self.head
			self.head = node
		self.length += 1

	def delete_from_beginning( self ):
		""" Delete a node from the starting of the list """
		# if list is empty
		if self.head is None:
			print( "List is empty!" )
			return False

		elif self.head == self.tail:
			item = self.head
			self.head = self.tail = None
			self.length -= 1
			return item.value

		else:
			item = self.head
			self.head = self.head.next
			self.length -= 1
			return item.value

	def insert_at_end( self, value ):
		""" Insert a node at the end of the list """
		node = Node( value )

		# if list is empty
		if self.tail is None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node
		self.length += 1

	def delete_from_end( self ):
		""" Delete a node from the end of the list """
		# if list is empty
		if self.tail is None:
			print( "List is empty!" )
			return False
		# list contains only one element
		elif self.tail == self.head:
			 item = self.tail
			 self.tail = self.head = None
			 self.length -= 1
			 return item.value
		# when list contains more than one item
		else:
			item  = self.tail
			start = self.head
			while start.next != self.tail:
				start = start.next
			self.tail = start
			self.tail.next = None
			self.length -= 1
			return item.value

	def insert_at_location( self, value, location ):
		node = Node( value )
		
		# if list is empty
		if self.head is None:
			# and location is first
			if location == 1:
				self.head = self.tail = node
				self.length += 1
				return True
			else:
				print( "Invalid location!" )
		
		# if list is not empty and insert at beginning
		elif location == 1:
			return self.insert_at_beginning( value )
		
		elif location == self.length + 1:
			return self.insert_at_end( value )
		
		else:
			count = 1
			previous = current = self.head
			
			while current is not None:
				if count == location:
					break
				count += 1
				previous = current
				current = current.next
				
			if count == location:
				node.next = current
				previous.next = node
				self.length += 1
			else:
				print( "Invalid Location!" )
				return False
			
	def delete_from_location( self, location ):
		""" Delete a node from a specific location """
		
		if self.length < location:
			print( "Invalid Location!" )
			return False
		
		# if list is empty
		if self.head is None:
			print( "List is empty!" )
			return False
		# if list contains only one element
		if location == 1:
			return self.delete_at_beginning()
		
		elif location == self.length:
			return self.delete_at_end()
			
		else:
			count = 1
			previous = self.head
			current = self.head
			
			while current is not None:
				if count == location:
					break
				previous = current
				current = current.next
				count += 1
				
			if count == location:
				previous.next = current.next
				item = current
				self.length -= 1
				return item.value
			else:
				print( "Location does not exists in the list" )
				return False
	

	def size( self ):
		""" returns the size of the linked list """
		return self.length

	def reverse( self ):
		""" Returns the reverse of a linked list """
		ll = LinkedList()
		
		start = self.head
		
		while start is not None:
			ll.insert_at_beginning( start.value )
			start = start.next
			
		return ll

class DNode( Node ):
	""" Node for doubly linked list """
	def __init__( self, value ):
		super().__init__( value )
		self.prev = None
		
class DoublyLinkedList( LinkedList ):
	""" A Doubly linked list """
	
	def __init__( self ):
		super().__init__()
		
	def insert_at_beginning( self, value ):
		node = DNode( value )
		
		# if list is empty
		if self.head is None:
			self.head = self.tail = node
			self.length += 1
		# if list contains only one element
		elif self.head == self.tail:
			node.next = self.head
			self.head = node
			self.tail.prev = node
			self.length += 1
		else:
			node.next = self.head
			self.head.prev = node
			self.head = node
			self.length += 1
			
	def delete_from_beginning( self ):
		# if list is empty
		if self.head is None:
			print( "List is empty!" )
			return False
		# if list contains only one element
		elif self.head == self.tail:
			self.head = self.tail = None
			self.length -= 1
		else:
			item = self.head
			self.head = self.head.next
			self.head.prev = None
			self.length -= 1
			return item.value
			
	def insert_at_end( self, value ):
		""" Insert at the end of the linked list """
		node = DNode( value )
		
		# if list is empty
		if self.head is None:
			self.head = self.tail = node
			self.length += 1
		# if list contains only one element
		elif self.head == self.tail:
			self.head.next = node
			node.prev = self.head
			self.tail = node
			self.length += 1
		else:
			node.prev = self.tail
			self.tail.next = node
			self.tail = node
			self.length += 1
			
	def delete_from_end( self ):
		""" Delete a node from the end of the list """
		# if list is empty
		if self.head is None:
			print( "List is empty!" )
			return False
		# if list contains only one element
		elif self.head == self.tail:
			item = self.tail
			self.head = self.tail = None
			self.length -= 1
			return item.value
		else:
			item = self.tail
			self.tail = self.tail.prev
			self.tail.next = None
			self.length -= 1
			return item.value
			
	def insert_at_location( self, value, location ):
		""" Insert a node at a particular position """
		node = DNode( value )
		
		# if list is empty
		if self.head is None:
			if location == 1:
				self.head = self.tail = node
				self.length += 1
			else:
				print( "Invalid location!" )
				return False
		# if location is first	
		elif location == 1:
			self.insert_at_beginning( value )
		# if location is at the end of the list, call insert_at_end method
		elif location == self.length + 1:
			self.insert_at_end( value )
		
		else:
			count = 1
			previous = current = self.head
			
			while current is not None:
				if count == location:
					break
				count += 1
				previous = current
				current = current.next
			
			if count == location:
				node.next = current
				node.prev = previous
				previous.next = node
				current.prev = node
	
	def delete_from_location( self, location ):
		""" Delete a node from a particular position """
		
		if location > self.length:
			print( "Invalid location" )
			return False
		
		# if list is empty
		if self.head is None:
			print( "List is empty!" )
			return False
		# if only one item is in the list
		elif self.head == self.tail:
			if location == 1:
				item = self.head
				self.head = self.tail = None
				self.length -= 1
				return item.value
			else:
				print( "Invalid Location!" )
				return False

		elif location == 1:
			self.delete_from_beginning()

		elif location == self.length:
			self.delete_from_end()

		else:
			count = 1
			previous = current = self.head
			
			while current is not None:
				if count == location:
					break
				count += 1
				previous  = current
				current = current.next
				
			if count == location:
				item = current
				previous.next = current.next
				(current.next).prev = previous
				self.length -= 1
				return item.value
			else:
				print( "Invalid location!" )
				return False
			
		
def main( option ):

	if ( option == 1 ):
		ll = LinkedList()
	else:
		ll = DoublyLinkedList()
	i = 1
	while i != 0:
		print( "Select the operation to perform: " )
		print( "1 -> traverse, 2 -> delete from beginning, 3 -> delete from end " )
		print( "4 -> delete from location, 5 -> insert at beginning, 6 -> insert at end" )
		print( "7 -> insert at location, 8 -> size of the list, 9 -> exit: " )
		response = int( input() )
		
		if response == 1: ll.traverse()
		elif response == 2: ll.delete_from_beginning()
		elif response == 3: ll.delete_from_end()
		elif response == 4:
			loc = int( input( "Enter the location of the item to be deleted: " ) )
			ll.delete_from_location( loc )
		elif response == 5:
			val = input( "Enter the item to insert: " )
			ll.insert_at_beginning( val )
		elif response == 6:
			val = input( "Enter the item to insert: " )
			ll.insert_at_end( val )
		elif response == 7:
			val = input( "Enter the value to insert: " )
			loc = int( input( "Enter the location: " ) )
			ll.insert_at_location( val, loc )
		elif response == 8: print( ll.size() )
		elif response == 9: i = 0
		else:
			print( "Invalid location" )
#			
#a = int( input( "Enter 1 for singly Linked list or any key for doubly linked list: " ) )
#main( a )
