""" CLRS GRAPHS """

from sys import maxsize

# ==============================================================================

class Vertex( object ):
	""" A vertex in the graph """
	
	def __init__( self, value ):
		self.value = value
		self.d_time = 0
		self.f_time = 0
		self.path = 0
		self.distance = 0
		self.predecessor = None
		
class CGraph( object ):
	""" A graph """
	
	def __init__( self ):
		self.adj_list = {}
		self.vertices = {}
		
	def has_vertex( self, vertex ):
		""" Returns True if vertex is in the graph, False otherwise """
		try:
			self.adj_list[vertex]
			return True
		except KeyError:
			return False
	
	def has_edge( self, start, end ):
		""" Returns True if there is an edge between start and end """
		if self.has_vertex( start ) and self.has_vertex( end ):
			try:
				if self.adj_list[start][end] is True and self.adj_list[start][end] is True:
					return True
				return False
			except KeyError:
				return False
		return False
				
	def add_vertex( self, vertex ):
		""" Adds vertex to the graph if not already present """
		if self.has_vertex( vertex ):
			return False
		else:
			self.adj_list[vertex] = {}
			self.vertices[vertex] = True
			return True
			
	def add_edge( self, start, end ):
		""" Adds an undirected edge """
		self.adj_list[start][end] = True
		self.adj_list[end][start] = True
	
	
	def remove_vertex( self, vertex ):
		if has_vertex( vertex ):
			for connected_vertex in self.adj_list[vertex]:
				remove_edge( connected_vertex, vertex )
			del self.adj_list[vertex][connected_vertex]
			del self.vertices[vertex]
			return True
		return False
	
	def remove_edge( self, start, end ):	
		if self.has_edge( start, end ):	
			del self.adj_list[start][end]
			del self.adj_list[end][start]
			return True
		return False
# ==============================================================================

G = CGraph()
a1 = Vertex(1)
a2 = Vertex(2)
a3 = Vertex(3)
a4 = Vertex(4)
a5 = Vertex(5)
a6 = Vertex(6)
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

# ==============================================================================
# helper functions
def print_level_info( hashtable ):
	for key in hashtable:
		print( key.value, hashtable[key]  )
	
def print_parent_info( hashtable ):
	for key in hashtable:
		if hashtable[key] is not None:
			print( key.value, hashtable[key].value )

def breadth_first_search( Adj, s ):
	""" Breadth first search as given in CLRS """
	level = {a1: 0}
	parent = {a1: None}
	i = 1
	frontier = [s]
	while frontier: # frontier not empty
		next = []
		for u in frontier:
			for v in Adj[u]:	
				if v not in level:
					level[v] = i
					parent[v] = u
					next.append( v )
		i += 1
		frontier = next
	return (level, parent)

# ==============================================================================

#level, parent = breadth_first_search( G.adj_list, a1 )
#print_level_info( level )
#print("Parent")
#print_parent_info( parent )

# ==============================================================================
## A Directed weighted Graph
class DiGraph( CGraph ):
	""" A directed weighted graph """
	def __init__(self):
		CGraph.__init__(self)
		self.weights = {}
		
	def add_directed_edge( self, start, end, weight ):
		""" Adds a directed edge into the graph """
		self.adj_list[start][end] = True
		self.weights[(start, end)] = weight
	
	def has_edge( self, start, end ):
		""" Returns True if there is an edge between start and end """
		if self.has_vertex( start ) and self.has_vertex( end ):
			try:
				if self.adj_list[start][end] is True:
					return True
				return False
			except KeyError:
				return False
		return False
	
	def remove_edge( self, start, end ):	
		""" Removes a directed edge from the graph """
		if self.has_edge( start, end ):	
			del self.adj_list[start][end]
			del self.weights[(start, end)]
			return True
		return False
	

""" FOR TOPOLOGICAL SORT AND DAG (DIRECTED ACYCLIC GRAPH) SHORTEST PATH """
def DFS_Visit( Adj, s, parent, time, topo ):
	""" Finds all vertices reachable from a single vertex """
	time += 1
	s.d_time = time
	for v in Adj[s]:
		if v not in parent:
			parent[v] = s
			DFS_Visit( Adj, v, parent, time, topo )
	time += 1
	s.f_time = time
	topo.append(s)
	
def CDFS( G ):
	""" Performs Depth First Search on the given graph and topologically sorts the vertices """
	parent = {}
	topo_result = []
	time = 0
	for s in G.vertices:
		if s not in parent:
			parent[s] = None
			DFS_Visit( G.adj_list, s, parent, time, topo_result )
	return parent, topo_result[::-1]
# ==============================================================================

G2 = DiGraph()
G2.add_vertex(a1)
G2.add_vertex(a2)
G2.add_vertex(a3)
G2.add_vertex(a4)
G2.add_vertex(a5)
G2.add_directed_edge(a1, a2, 5)
G2.add_directed_edge(a1, a4, 2)
G2.add_directed_edge(a1, a3, -1)
G2.add_directed_edge(a2, a3, 4)
G2.add_directed_edge(a4, a3, -5)
G2.add_directed_edge(a3, a5, 7)

#parent, topo_result = CDFS( G2 )
#print("parent")
#print_parent_info( parent )
#print( printCurrentPath( topo_result[] ) )

## =============================================================================
## DAG SHORTEST PATH
def initialize_single_source(G, s):
	""" Sets the distance of all vertices in G to positive infinity (a large int) """
	for v in G.vertices:
		v.distance = 200000000
		v.predecessor = None
	s.distance = 0

def Relax(G, u, v):
	""" update the distance between u and v if its shorter than previous distance """
	print(u.value, v.value)
	if v.distance > u.distance + G.weights[(u, v)]:
		v.distance = u.distance + G.weights[(u, v)]
		v.predecessor = u 

def DAG_shortest_path(G, s):
	""" 
		DAG (Directed Acyclic Graph) is a directed graph which has no cycles
		Finds the shotest path from source s to all the reachable vertices.
	"""
	p, topological_sorted = CDFS(G)
	p = None
	initialize_single_source(G, s)
	print(topological_sorted)
	for vertex in topological_sorted:
		for v in G.adj_list[vertex]:
			Relax(G, vertex, v)
	return topological_sorted[-1]
## =============================================================================

## DIJKSTRA SHORTEST PATH ALGORITHM
def Dijkstra(G, s):
	""" 
		Finds the shortest path in a directed graph (with positive weights)
		from source vertex s to all the other vertices
	"""
	initialize_single_source(G, s)
	S = []
	a = list(G.vertices)
	a.sort(key=lambda v: v.distance) # Sort vertices according to their distances
	count = len(a)
	
	while count > 0:
		u = a[len(a) - count]
		S.append(u)
		count -= 1
		for v in G.adj_list[u]:
			Relax(G, u, v)
## =============================================================================

## BELLMAN-FORD SHORTEST PATH ALGORITHM
def Bellman_Ford(G, s):
	"""
		Same as Dijkstra. But works for negative weights too.
	"""
	initialize_single_source(G, s)
	for i in range(len(G.vertices)):
		for e in G.weights:
			Relax(G, e[0], e[1])
	for e in G.weights:
		if e[1].distance > e[0].distance + G.weights[e]:
			return False
	return True

## =============================================================================

## =============================================================================
## All Pairs Shortest Path Algorithm - Floyd-Warshall Algorithm

def floyd_warshall(W):  
    """ Floyd-Warshall algorithm  """
    l = len(W)
    d = W

    for k in range(l):
        for i in range(l):
            for j in range(l):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
    
    print_matrix(d)


def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end="\t")
        print()

# ==============================================================================
G3 = DiGraph()
s = Vertex("s")
t = Vertex("t")
x = Vertex("x")
y = Vertex("y")
z = Vertex("z")
G3.add_vertex(s)
G3.add_vertex(t)
G3.add_vertex(x)
G3.add_vertex(y)
G3.add_vertex(z)
G3.add_directed_edge(s, t, 10)
G3.add_directed_edge(s, y, 5)
G3.add_directed_edge(t, y, 2)
G3.add_directed_edge(t, x, 1)
G3.add_directed_edge(y, t, 3)
G3.add_directed_edge(y, z, 2)
G3.add_directed_edge(y, x, 9)
G3.add_directed_edge(x, z, 4)
G3.add_directed_edge(z, x, 6)

W = [[0, 10, maxsize, 5, maxsize],
     [maxsize, 0, 1, 2, maxsize],
     [maxsize, maxsize, 0, maxsize, 4],
     [maxsize, 3, 9, 0, 2],
     [maxsize, maxsize, 6, maxsize, 0]]

W2 = [[0, 3, 8, maxsize, -4],
      [maxsize, 0, maxsize, 1, 7],
      [maxsize, 4, 0, maxsize, maxsize],
      [2, maxsize, -5, 0, maxsize],
      [maxsize, maxsize, maxsize, 6, 0]]
