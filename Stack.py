""" Stack implementation in python """

class Stack( object ):
	""" Implementation of stack data structure """

	def __init__( self ):
		""" Initialize the list storage which will contain the elements of the stack. """
		self.storage = {}
		self.MAX = 10
		self.position = -1

	def push( self, value ):
		"""
			Pushes the value on top of stack.
			Returns True if value is inserted, False otherwise. 
		"""
		if ( self.position < self.MAX - 1 ):
			self.position += 1
			self.storage[self.position] = value
			return True
		else:
			print( "Stack is Full!" )
			return False

	def pop( self ):
		""" Pops the top element out of the stack """
		if ( self.position == -1 ):
			print( "Stack is empty!" )
			return False
		else:
			item = self.storage[self.position]
			del self.storage[self.position]
			self.position -= 1
			return item
	
	def top( self ):
		""" Returns the top element of the stack without deleting it """
		return self.storage[self.position]
	
	def size( self ):
		""" Returns the size of the stack """
		return self.position + 1


# Infix to Postfix notation
def reverse_polish_notation( infix ):
	""" Convert an expression from infix to postfix """
	stack = Stack()
	stack.push( "(" )
	infix += ")"
	postfix = ""
	
	for char in infix:
		
		if ( stack.size == 0 ):
			return postfix
			
		# if an operator is encountered, repeatedly pop from stack operators
		# with precedence equal to or greater than or equal to current operator
		if ( char == "+" or char == "-" or char == "/" or char == "*" or char == "^" ):
			
			# if operator is + or -, pop until a left parenthesis is found
			if ( char == "+" or char == "-" ):
				operator = stack.top()
				while ( operator != "(" ):
					# pop the operator
					oper = stack.pop()
					postfix += str( oper )
					operator = stack.top()
			
			elif ( char == "*" or char == "/" ):
				operator = stack.top()
				while ( operator == "*" or operator == "/" or operator == "^" ):
					oper = stack.pop()
					postfix += str( oper )
					operator = stack.top()
					
			elif ( char == "^" ):
				operator = stack.top()
				while ( operator == "^" ):
					oper = stack.pop()
					postfix += str( oper )
					operator = stack.top()
			stack.push( char )
		
		# if a left parenthesis is encountered, push it onto stack
		elif ( char == "(" ):
			stack.push( char )
			
		# if a right parenthesis is encountered, repeatedly pop from stack
		# until a left parenthesis is encountered
		elif ( char == ")" ):
			operator = stack.top()
			while ( operator != "(" ):
				oper = stack.pop()
				postfix += str( oper )
				operator = stack.top()
			# remove the left parenthesis
			stack.pop()
		
		# if an operand is encountered add it to postfix 
		else:
			postfix += char
			
	return postfix

# Testing of Stack Data Structure
import unittest

class TestStack( unittest.TestCase ):
	""" Testing of method of stack data structure """
	
	def test_empty_stack( self ):
		stack = Stack()
		self.assertEqual( stack.size(), 0 )
	
	def test_underflow_condition( self ):
		stack = Stack()
		self.assertFalse( stack.pop() )
	
	def test_push_one_element( self ):
		stack = Stack()
		self.assertTrue( stack.push( 10 ) )

	def test_pop_one_element( self ):
		stack = Stack()
		stack.push( 5 )
		self.assertEqual( stack.pop(), 5 )
		
	def test_full_stack( self ):
		stack = Stack()
		# insert 10 elements in the stack
		for i in range( 10 ):
			stack.push( i )
		
		self.assertEqual( stack.size(), 10 )
		# empty the stack
		for i in range( 10 ):
			stack.pop()
		
		self.assertEqual( stack.size(), 0 )
		
	def test_overflow_condition( self ):
		stack = Stack()
		# insert 11 elements as maximum size of stack is 10
		for i in range( 10 ):
			stack.push( i )
			
		self.assertFalse( stack.push( 20 ) )
	
if __name__ == '__main__':
	unittest.main()
