""" Implementation of Graph data structure """

class Node( object ):
	""" A node hasVertex some information """
	
	def __init__( self, value ):
		""" 
			Status is used in graph traversal. Its value could be 0, 1 or 2
			0 -> Ready State, 1 -> Waiting State, 2 -> Processed State
		"""
		self.value = value
		self.status = 0		# used in Graph traversal

class Graph( object ):
	""" 
		A graph is a set nodes connected with edges.
		This graph is an Undirected graph
	"""
	
	def __init__( self ):
		self.graph = {}
		
	def hasVertex( self, node ):
		""" Returns True if node is in the graph, false otherwise """
		try:
			self.graph[node]
			return True
		except KeyError:
			return False
	
	def hasEdge( self, start, end ):
		""" Returns True if there is an edge between start and end, else False """
		if self.hasVertex( start ) and self.hasVertex( end ):
			try:
				return True
			except KeyError:
				return False
			
		return False
	
	def addVertex( self, node ):
		""" Adds a vertex to the graph if not already exists """
		if not self.hasVertex( node ):
			
			self.graph[node] = {"edges": {}}
			#self.graph[node][edges] = {}
			return True
		print( "Vertex already Exists" )
		return False
		
	def addEdge( self, start, end ):
		""" Adds an edge between two vertices if not already exists """
		if self.hasVertex( start ) and self.hasVertex( end ):	
			self.graph[start]["edges"][end] = True
			self.graph[end]["edges"][start] = True
			return True
		print( "Given vertex doesn't exists in the graph'" )
		return False
		
	def removeVertex( self, node ):	
		""" Removes the given vertex from the graph """
		if self.hasVertex( node ):
			for connectedNode in self.graph[node]["edges"]:
				self.removeEdge( node, connectedNode )
			del self.graph[node]
			return True
		print( "Vertex doesn't exists" )
		return False
			
	def removeEdge( self, start, end ):
		""" Removes the edge between two given vertex """
		if self.hasEdge( start, end ):
			del self.graph[start]["edges"][end]
			del self.graph[end]["edges"][start]
			return True
		return False
		

def BFS( G, start, end ):
	""" Searches a node in the graph using Breadth First Search. """
	# Set all nodes to ready state (status = 0)
	for nodes in G.graph:
		nodes.status = 0
	queue = []
	queue.append(start)
	path = []
	start.status = 1
	while len( queue ) != 0:
		current = queue.pop(0)
		path.append(current.value)
		# set status to process state (status = 2)
		current.status = 2
		
		print( "Current Path: ", path )
		# if current is the end node, return the path traced
		if current == end:
			return path
		# add all the neighbours of current in ready state to the queue
		else:
			for vertex in G.graph[current]["edges"]:
				if vertex.status == 0:
					# set status to waiting state (status = 1)
					queue.append(vertex)
					vertex.status = 1
	return False
	

def DFS( G, start, end ):
	""" Searches a node in a graph using Depth First Search """
	# sets status of all nodes to ready state (status = 1)
	for nodes in G.graph:
		nodes.status = 0
	
	stack = []
	stack.append( start )
	path = []
	start.status = 1
	while len( stack ) != 0:
		# pop the last element from the stack and set it to process state
		current = stack.pop()
		current.status = 2
		path.append(current.value)
		print( "Current Path: ", path )
		# if current element is the end, return the traced path
		if current == end:
			return path
		# push all the neighbours of current in ready state to the stack
		else:
			for vertex in G.graph[current]["edges"]:
				if vertex.status == 0:
					# set status to waiting state (status = 1)
					stack.append( vertex )
					vertex.status = 1
					
	return False


def printCurrentPath( path ):
	""" Accepts a list of nodes and prints then values of the nodes """
	print( "Path: ", end="" )
	for node in path:
		print( node.value, end=" " )
	print()

def ShortestDFS( G, start, end, path = [], shortest = None ):
	""" Finds the shortest path from start to end using DFS """
	path = path + [start]
	
	if start == end:
		return path
	else:
		for vertex in G.graph[start]["edges"]:
			#printCurrentPath( path )
			if vertex not in path:
				if shortest is None or len(path) < len(shortest):
					newPath = ShortestDFS( G, vertex, end, path, shortest )
					if newPath is not None:
						shortest  = newPath
						
	return shortest

	
## Simulation
G = Graph()
a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)
a6 = Node(6)
G.addVertex(a1)
G.addVertex(a2)
G.addVertex(a3)
G.addVertex(a4)
G.addVertex(a5)
G.addEdge(a1,a2)
G.addEdge(a1,a5)
G.addEdge(a3,a2)
G.addEdge(a4,a2)
G.addEdge(a5,a2)
G.addEdge(a3,a4)
G.addEdge(a4,a5)

print( BFS(G, a1, a6) )
print( DFS(G, a1, a3) )
printCurrentPath( ShortestDFS(G, a1, a3) )
