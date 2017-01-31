""" Implementation of Graph data structure """

class Node( object ):
	""" A node has_vertex some information """
	
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
		
	def has_vertex( self, node ):
		""" Returns True if node is in the graph, false otherwise """
		try:
			self.graph[node]
			return True
		except KeyError:
			return False
	
	def has_edge( self, start, end ):
		""" Returns True if there is an edge between start and end, else False """
		if self.has_vertex( start ) and self.hasVertex( end ):
			try:
				if self.graph[start]["edges"][end] is True and self.graph[end]["edges"][stack] is True:
					return True
				else:
					return False
			except KeyError:
				return False
			
		return False
	
	def add_vertex( self, node ):
		""" Adds a vertex to the graph if not already exists """
		if not self.has_vertex( node ):
			
			self.graph[node] = {"edges": {}}
			#self.graph[node][edges] = {}
			return True
		print( "Vertex already Exists" )
		return False
		
	def add_edge( self, start, end ):
		""" Adds an edge between two vertices if not already exists """
		if self.has_vertex( start ) and self.hasVertex( end ):	
			self.graph[start]["edges"][end] = True
			self.graph[end]["edges"][start] = True
			return True
		print( "Given vertex doesn't exists in the graph'" )
		return False
		
	def remove_vertex( self, node ):	
		""" Removes the given vertex from the graph """
		if self.has_vertex( node ):
			for connectedNode in self.graph[node]["edges"]:
				self.remove_edge( node, connectedNode )
			del self.graph[node]
			return True
		print( "Vertex doesn't exists" )
		return False
			
	def remove_edge( self, start, end ):
		""" Removes the edge between two given vertex """
		if self.has_edge( start, end ):
			del self.graph[start]["edges"][end]
			del self.graph[end]["edges"][start]
			return True
		return False


class DiGraph:
    """ A directed graph """

    def __init__(self):
        self.list = {}

    def has_vertex(self, v):
        """ Returns True if v is in graph, False otherwise """
        try:
            self.list[v]
            return True
        except KeyError:
            return False

    def add_vertex(self, v):
        """ Adds v into graph if not already present """
        if self.has_vertex(v):
            return False
        self.list[v] = {}
        return True

    def has_edge(self, start, end):
        """ Returns True if there is an edge between start and end """
        if self.has_vertex(start) and self.has_vertex(end):
            try:
                self.list[start][end]
                return True
            except KeyError:
                return False
        return False

    def add_edge(self, start, end):
        """ Adds the edge (start, end) in the graph """
        if self.has_vertex(start) and self.has_vertex(end):
            self.list[start][end] = 1
            return True
        return False

    def remove_edge(self, start, end):
        """ Removes edge (start, end) from the graph if present """
        if self.has_vertex(start) and self.has_vertex(end):
            del self.list[start][end]
            return True
        return False

    def remove_vertex(self, v):
        """ Removes vertex v from graph if present """
        if self.has_vertex(v):
            for u in self.list:
                try:
                    del self.list[u][v]
                except KeyError:
                    pass

            del self.list[v]
            return True
        return False


# ==============================================================================
# Check For cycles in a DiGraph
def visit_neighbours(G, s):
    """ Visits the neighbours of s """
    for u in G.list[s]:
        #print("child", u.value)
        if u.status == 1:
            return False
        else:
            u.status = 1 
            visit_neighbours(G, u)
    s.status = 3
    return True

def have_cycles(G):
    """ Returns True if graph G has cycles """
    for i in G.list.keys():
        i.status = 0

    for v in G.list.keys():
        if v.status == 1:
            return True
        else:
            v.status = 1
            if visit_neighbours(G, v) == False:
                return True
    return False


DG = DiGraph()

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

DG.add_vertex(a)
DG.add_vertex(b)
DG.add_vertex(c)
DG.add_vertex(d)
DG.add_vertex(e)
DG.add_vertex(f)
DG.add_vertex(g)

DG.add_edge(a,b)
DG.add_edge(a,d)
DG.add_edge(b,c)
DG.add_edge(e,c)
DG.add_edge(d,b)
DG.add_edge(c,f)
DG.add_edge(e,g)
DG.add_edge(f,g)
DG.add_edge(g,d)

x = have_cycles(G)

# ==============================================================================
# Breadth First Search
    
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

# ==============================================================================

# ==============================================================================
# Depth First Search

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

# ==============================================================================
	
## Simulation
G = Graph()
a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)
a6 = Node(6)
G.add_vertex(a1)
G.add_vertex(a2)
G.add_vertex(a3)
G.add_vertex(a4)
G.add_vertex(a5)
G.add_edge(a1,a2)
G.add_edge(a1,a5)
G.add_edge(a3,a2)
G.add_edge(a4,a2)
G.add_edge(a5,a2)
G.add_edge(a3,a4)
G.add_edge(a4,a5)

