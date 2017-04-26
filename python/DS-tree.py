""" Implementation of a Binary Tree """

class Node(object):
	""" A node contains some information """
	
	def __init__(self, value):
		self.value = value
		self.parent = None
		self.left = None
		self.right = None


def inorder(root):
	""" Prints the inorder traversal of a tree """
	if root != None:
		inorder(root.left)
		print(root.value, end=" ")
		inorder(root.right)

def preorder(root):
	""" Prints the preorder traversal of a tree """
	if root != None:
		print(root.value, end=" ")
		preorder(root.left)
		preorder(root.right)

def postorder(root):
	""" Prints the postorder traversal of a tree """
	if root != None:
		postorder(root.left)
		postorder(root.right)
		print(root.value, end=" ")
		


class BinarySearchTree(object):
	""" 
		Binary search tree is a binary tree in which each node > left child and 
		<= right child
	"""
	def __init__(self):
		self.root = None
		self.length = 0
	
	def length(self):
		return self._length


def TreeSearch(x, key):
	""" Search the given node in a Binary Search Tree """
	if x is None or key == x.value:
		return x
	elif x.value < key:
		return TreeSearch(x.right, key)
	else:
		return TreeSearch(x.left, key)

def TreeMinimum(x):
	""" Finds the minimum element in a binary search tree """
	while x.left is not None:
		x = x.left
	return x
	
def TreeMaximum(x):
	""" Finds the maximum element in a binary search tree """
	while x.right is not None:
		x = x.right
	return x
	
def TreeSuccessor(x):
	""" Finds the successor of x in a binary Search Tree """
	if x.right is not None:
		return TreeMinimum(x)
	
	y = x.parent
	while (y is not None and x == y.right):
		x = y
		y = y.parent
	return y
	
def TreePredecessor(x):
	""" Find the predecessor of x in a binary search tree """
	if x.left is not None:
		return TreeMaximum(x)
		
	y = x.parent
	while (y is not None and x == y.right):
		x = y
		y = y.parent
	return y

def TreeInsert(T, z):
	""" Inserts node x in a binary search tree T """
	y = None
	x = T.root
	# find the right position to insert node z
	while x is not None:
		y = x
		if z.value < x.value:
			x = x.left
		else:
			x = x.right
	# insert node z in BST T
	z.parent = y 
	if y is None:
		T.root = z		# tree is empty
	elif z.value < y.value:
		y.left = z 
	else: y.right = z 

def Transplant(T, u, v):
	""" Replaces node v with node u """
	if u.parent is None:
		T.root = v 
	elif u == u.parent.left: # if u is left node of its parent
		u.parent.left = v 
	else:
		u.parent.right = v 
	
	if v is not None:
		v.parent =  u.parent

def TreeDelete(T, z):
	""" Deletes a node z from a BST T """
	# if left subtree of z is empty replace z with its right child
	if z.left is None:
		Transplant(T, z, z.right)
	# if right subtree of z is empty replace z with its left child
	elif z.right is None:
		Transplant(T, z, z.left)
	else:
		# find the successor
		y = TreeMinimum(z.right)
		# if its not the right child of z
		if y.parent != z:
			# replace y with its right child, y has no left child being successor
			Transplant(T, y, y.right)
			# connect y with the right subtree z
			y.right = z.right 
			y.right.parent =  y
		# replace z with y
		Transplant(T, z, y)
		# connect y with the left subtree of z
		y.left = z.left 
		y.left.parent = y


def lowest_common_ancestor(x, y):
	""" Find the lowest common ancestor of x and y in a tree """
	p1 = [x]	# contains parents of x including x
	p2 = [y]	# contains parents of y including y
	
	node1, node2 = x, y
	# find all the ancestors of x
	while node1.parent is not None:
		p1.append(node1.parent)
		node1 = node1.parent
	# find all the ancestors of y
	while node2.parent is not None:
		p2.append(node2.parent)
		node2 = node2.parent

	LCA = None
	while p1 and p2:	# while p1 and p2 are not empty
		a = p1.pop()
		b = p2.pop()
		if a == b:		# if nodes are same update lowest common ancestor
			LCA = a
		else:
			break		
	return LCA


node1 = Node(10)
node2 = Node(5)
node3 = Node(2)
node4 = Node(8)
node5 = Node(20)
node6 = Node(15)
node1.left = node2 
node1.right = node5 
node2.parent = node1 
node2.left = node3 
node2.right = node4 
node3.parent = node2 
node4.parent = node2 
node5.parent = node1 
node5.left = node6 
node6.parent = node5 

print("Inorder: ", end=" ")
inorder(node1)
print()
print("Preorder: ", end=" ")
preorder(node1)
print()
print("Postorder: ", end=" ")
postorder(node1)
print()
	

