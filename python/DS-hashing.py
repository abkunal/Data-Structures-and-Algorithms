""" Hashing and String Matching in Python """


class direct_address_table( object ):
	""" 
		Using a direct address table to store data to store integers
		from 0 to size.
	"""
	
	def __init__( self, size ):
		self._storage = [None for i in range( size )] # initialize all slots to None
		
	def insert( self, key ):
		""" Inserts a key in the direct address table """
		try:
			self._storage[key] = key
		except IndexError:
			print( "Key out of range" )
			return False
			
		return True
	
	def get_key( self, key ):
		if self._storage[key] is None:
			print( "Key doesn't exists'" )
			return False
		
		return self._storage[key]
	
	def delete( self, key ):
		""" delete the specified key from the table """
		key = self._storage[key]
		self._storage[key] = None
		
		return key
		
	def show_data( self ):
		""" Shows the data inside the table """
		for key in self._storage:
			if key is not None:
				print( key, end=" " )
				
		return True
		


import unittest
class test_direct_address_table( unittest.TestCase ):
	""" Testing direct_address_table class """
	table = direct_address_table( 100 )
	
	def test_empty_table( self ):
		self.assertFalse( self.table.get_key( 10 ) )
	
	def test_one_value( self ):
		self.table.insert( 20 )
		self.assertEqual( self.table.get_key( 20 ), 20 )
		
	def test_one_value_deleted( self ):
		self.table.delete( 20 )
		self.assertFalse( self.table.get_key( 20 ) )
		
	def test_out_of_range_value( self ):
		self.assertFalse( self.table.insert( 120 ) )
		
#if __name__ == "__main__":
#	unittest.main()

class doubly_node( object ):
	""" Node in a doubly linked list """
	
	def __init__( self, key, value ):
		self._key = key
		self._value = value
		self.next = None
		self.prev = None
		
	def get_key( self ):
		return self._key
		
	def get_value( self ):
		return self._value


class doubly_linked_list( object ):
	""" Implementation of a doubly linked list """
	
	def __init__( self ):
		self._head = None
		self._tail = None
		self._length = 0
		
	def size( self ):
		return self._length
		
	def insert_at_beginning( self, key, value ):
		""" inserts the value at the beginning of the list """
		node = doubly_node( key, value )
		
		if self._head is None:              # list is empty
			self._head = self._tail = node
		else:
			node.next = self._head
			self._head = node
		self._length += 1
		return True
			
	def delete_beg( self ):
		# list is empty
		if self._head is None:
			return False
		# list contains only one element
		elif self._head == self._tail:
			self._head = self._tail = None
			self._length -= 1
		else:
		# list is not empty and contains more than one element
			self._head = self._head.next
			self._head.prev = None
			
		return True
		
	def delete_end( self ):
		# list is empty
		if self._head is None:
			return False
		# list contains only one element
		elif self._head == self._tail:
			self._head = self._tail = None
			self._length -= 1
		else:
			self._tail = self._tail.prev
			self._tail.next = None
			self._length -= 1
		return True
		
	def delete_node( self, key ):
		""" Deletes the node with the given key """
		
		# if list is empty
		if self._head is None:
			return False
		# when list contains a single element
		elif self._head.get_key() == key:
			return self.delete_beg()
			
		elif self._tail.get_key() == key:
			return self.delete_end()
		
		elif self._head == self._tail:
			return False
		
		else:
			cur = prev = self._head
			
			while cur is not None:
				if cur.get_key() == key:
					prev.next = cur.next
					cur.next.prev = prev
					self._length -= 1
					return True
				prev = cur
				cur = cur.next
		
		return False
		
	def get_node_value( self, key ):
		""" Returns the value associated with the given key """
		temp = self._head
		while temp is not None:
			if temp.get_key() == key:
				return temp.get_value()
			temp = temp.next
				
		return False


class hashtable( object ):
	""" Implementation of hashtable in python """
	
	def __init__( self, size = 11 ):
		self.storage = size * [doubly_linked_list()]
		self._size = 0
		
	def hash_function( self, key ):
		""" Using division method """
		prime = 11
		return key % prime
		
	def insert( self, key, value ):
		""" Inserts the given key in the table """
		bucket = self.hash_function( key )
		self.storage[bucket].insert_at_beginning( key, value )
		self._size += 1
		return True
		
	def search( self, key ):
		""" searches the value of the given key """
		bucket = self.hash_function( key )
		return self.storage[bucket].get_node_value( key )
		
	def delete( self, key ):
		bucket = self.hash_function( key )
		count = 0
		print( key )
		if self.storage[bucket].delete_node( key ):
			self._size -= 1
			count += 1
			print( count )
		else:
			
			raise KeyError("Key doesn't exists'")
				
		
	def size( self ):
		return self._size
		
		
## String Matching algorithms

def naive_substring_match( sub, string ):
	""" Matches the substring sub in the given string """
	sub_length = len( sub )
	for i in range( len(string) - sub_length ):
		if sub == string[i: i + sub_length]:
			return i
	
	return False
	
#print(naive_substring_match( "k", "unkasc" ))
#print(naive_substring_match( "kunal", "fsdfsdfkunalsdcsdcsd" ))
#print(naive_substring_match( "sdfsdfsdf", "sdfsd" ))


def Karp_Rabin_Algorithm1( sub, string ):
	""" 
		Karp-Rabin Algorithm using different hashing technique
		sub: string to be searched
		string: the string form which to search
		Returns the starting index of the substring in string if sub exists
		False otehrwise
	"""
	sub_hash = [ord(c) for c in sub]
	
	string_hash = [ord(c) for c in string[:len(sub)]]
	
	if sub_hash == string_hash:
		print( sub_hash, string_hash )
		return 0
		
	for i in range( len(sub), len(string) ):
		string_hash.pop(0)		# delete first char
		string_hash.append( ord(string[i]) )
		
		if sub_hash == string_hash:
			if sub == string[i-len(sub)+1:i+1]:
				return i - len(sub) + 1
				
	return False
			
	
def Karp_Rabin_Algorithm2( sub, string ):
	""" 
		Karp-Rabin Algorithm using different hashing technique
		sub: string to be searched
		string: the string form which to search
		Returns the starting index of the substring in string if sub exists
		False otehrwise
	"""
	sub_hash = sum([ord(c) for c in sub])
	
	string_hash = sum([ord(c) for c in string[:len(sub)]])
	
	if sub_hash == string_hash:
		if sub == string[:len(sub)]:
			return 0
	
	string_part = []
	
	for i in range(len(sub)):
		string_part.append(string[i])
	
	for i in range( len(sub), len(string) ):
		a = string_part.pop(0)
		string_part.append(string[i])
		
		string_hash -= ord(a)
		string_hash += ord(string[i])
		if sub_hash == string_hash:
			if sub == string[i-len(sub)+1: i+1]:
				return i - len(sub) + 1
		
	return False
		
