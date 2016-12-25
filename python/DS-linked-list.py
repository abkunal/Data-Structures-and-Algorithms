""" Implementation of linked list """

class Node( object ):
	""" Creates a node """

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

	def delete_at_beginning( self ):
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

	def delete_at_end( self ):
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
		if location == 1:
			node.next = self.head
			self.head = node
			self.length += 1
			return True
		
		count = 1
		start = self.head
		while start.next is not None:
			if count == location - 1:
				break
			count += 1
			start = start.next
		
		if count == location - 1:
			node.next = start.next
			start.next = node
			if self.length == count + 1:
				self.tail = node
			self.length += 1
			return True
		else:
			print( "Invalid Location second!" )
			return False

	def delete_at_location( self, location ):
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
			if self.head == self.tail:
				item = self.head
				self.head = self.tail = None
				self.length -= 1
				return item.value
			else:
				item = self.head
				self.head = self.head.next
				self.length -= 1
				return item.value
				
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
				if self.length == count:
					self.tail = previous
				self.length -= 1
				return item.value
				
				
			else:
				print( "Location does not exists in the list" )
				return False
	

	def size( self ):
		""" returns the size of the linked list """
		return self.length


def main():
	ll = LinkedList()
	i = 1
	while i != 0:
		print( "Select the operation to perform: " )
		print( "1 -> traverse, 2 -> delete from beginning, 3 -> delete from end " )
		print( "4 -> delete from location, 5 -> insert at beginning, 6 -> insert at end" )
		print( "7 -> insert at location, 8 -> size of the list, 9 -> exit: " )
		response = int( input() )
		
		if response == 1: ll.traverse()
		elif response == 2: ll.delete_at_beginning()
		elif response == 3: ll.delete_at_end()
		elif response == 4:
			loc = int( input( "Enter the location of the item to be deleted: " ) )
			ll.delete_at_location( loc )
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
			
main()
