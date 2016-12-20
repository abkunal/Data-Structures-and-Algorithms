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
		
	def content( self ):
		return self.storage


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

def test_stack():
	stack1 = Stack()
	stack.push( 10 )
	print stack.size()
	return stack.content()
