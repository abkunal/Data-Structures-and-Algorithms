""" Implementation of a Binary Tree """

class Node( object ):
	""" A node contains some information """
	
	def __init__( self, value ):
		self._value = value
		self._parent = None
		self._left = None
		self._right = None
		
	def get_value( self ):
		return self._value
	
	def get_parent( self ):
		return self._parent
		
	def get_left( self ):
		return self._left
		
	def get_right( self ):
		return self._right
	
	def set_parent( self, parent ):
		self._parent = parent
	
	def set_left( self, left ):
		self._left = left
		
	def set_right( self, right ):
		self._right = right


def inorder( root ):
	""" Prints the inorder traversal of a tree """
	if root != None:
		inorder( root.get_left() )
		print( root.get_value(), end=" " )
		inorder( root.get_right() )

def preorder( root ):
	""" Prints the preorder traversal of a tree """
	if root != None:
		print( root.get_value(), end=" " )
		preorder( root.get_left() )
		preorder( root.get_right() )

def postorder( root ):
	""" Prints the postorder traversal of a tree """
	if root != None:
		postorder( root.get_left() )
		postorder( root.get_right() )
		print( root.get_value(), end=" " )
		

def main():
	node1 = Node( 10 )
	node2 = Node( 5 )
	node3 = Node( 2 )
	node4 = Node( 8 )
	node5 = Node( 20 )
	node6 = Node( 15 )
	node1.set_left( node2 )
	node1.set_right( node5 )
	node2.set_parent( node1 )
	node2.set_left( node3 )
	node2.set_right( node4 )
	node3.set_parent( node2 )
	node4.set_parent( node2 )
	node5.set_parent( node1 )
	node5.set_left( node6 )
	node6.set_parent( node5 )
	
	print( "Inorder: ", end=" " )
	inorder( node1 )
	print()
	print( "Preorder: ", end=" " )
	preorder( node1 )
	print()
	print( "Postorder: ", end=" " )
	postorder( node1 )
	print()
	
main()
