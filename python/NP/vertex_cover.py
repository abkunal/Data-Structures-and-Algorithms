""" Vertex Cover NP-Complete Problem """

## A vertex cover of a graph is a subset of minimum number of vertices of the 
## graph which covers all the edges of the graph


class UndirectedGraph:
    """ An undirected graph """

    def __init__(self):
        self._vertices = set()
        self._edges = {}        # format -> {(u,v): 1}
    
    def get_vertices(self):
        return self._vertices

    def get_edges(self):
        return self._edges

    def has_vertex(self, vertex):
        """ Returns True if graph contains the given vertex, False otherwise """
        return vertex in self._vertices

    def has_edge(self, start, end):
        """ Returns True if there's an edge (start, end) or (end, start) """
        return (start, end) in self._edges or (end, start) in self._edges

    def add_vertex(self, vertex):
        """ Adds vertex in the graph if not already present """
        if self.has_vertex(vertex) is False:
            self._vertices.add(vertex)
            return True
        return False

    def add_edge(self, start, end):
        """ Adds an edge (start, end) in the graph if not already present """
        if self.has_edge(start, end) is False:
            self._edges[(start, end)] = 1
            return True
        return False

    def remove_edge(self, start, end):
        """ Removes the edge (start, end) from the graph if exists in the graph """
        if self.has_edge(start, end):
            if (start, end) in self._edges:
                del self._edges[(start, end)]
            else:
                del self._edges[(end, start)]
            return True
        return False

    def remove_vertex(self, vertex):
        """ Removes the given vertex if exists in the graph """
        if self.has_vertex(vertex) is True:
            self._vertices.remove(vertex)
            
            # Removes all the edges associated with the given vertex
            edges = list(self._edges.keys())
            for edge in edges:
                if vertex in edge:
                    self.remove_edge(edge[0], edge[1])


G = UndirectedGraph()

G.add_vertex(1)
G.add_vertex(2)
G.add_vertex(3)
G.add_vertex(4)
G.add_vertex(5)
G.add_vertex(6)
G.add_vertex(7)
G.add_vertex(8)
G.add_vertex(9)
G.add_vertex(10)
G.add_vertex(11)
G.add_vertex(12)
G.add_vertex(13)
G.add_vertex(14)
G.add_vertex(15)
G.add_vertex(16)
G.add_vertex(17)
'''
G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(1,4)
G.add_edge(2,3)
G.add_edge(2,4)
G.add_edge(3,4)
G.add_edge(2,5)
'''

G.add_edge(1,7)
G.add_edge(1,9)
G.add_edge(1,12)
G.add_edge(2,7)
G.add_edge(2,9)
G.add_edge(2,13)
G.add_edge(3,7)
G.add_edge(3,10)
G.add_edge(3,14)
G.add_edge(4,8)
G.add_edge(4,10)
G.add_edge(4,15)
G.add_edge(5,8)
G.add_edge(5,11)
G.add_edge(5,16)
G.add_edge(6,8)
G.add_edge(6,11)
G.add_edge(6,17)

# ==============================================================================
# Approximation Vertex Cover Algorithm
def approx_vertex_cover(G):
    """ 
        Takes an undirected graph as the input and returns an approximate vertex
        cover of the graph.
        Returns a set of vertices that covers all the edges.
    """
    assert type(G) == UndirectedGraph

    cover = set()
    edges =  dict(G.get_edges())

    while edges != {}:
        e = edges.popitem()[0]
        keys = list(edges.keys())
        cover.add(e[0])
        cover.add(e[1])

        for key in keys:
            if e[0] in key or e[1] in key:
                del edges[key]

    return cover
# ==============================================================================

print("Approximate Vertex Cover: ", approx_vertex_cover(G))

# ==============================================================================
# Bounded Tree Search Algorithm for k-Vertex Cover problem
def bounded_tree_search_vertex_cover(edges, k, cover):
    """"
        A Fixed Parameter Tractibility algorithm.
        Bounded Tree Search Method to solve k-Vertex Cover problem.
        Returns True if there is a vertex cover of size k in the given graph.
    """
    assert type(edges) == dict and type(k) == int and type(cover) == set
    if k == 0:
        return len(edges) == 0
    elif len(edges) == 0:
        return True
    else:
        # take an edge (u,v) from graph
        u,v = edges.popitem()[0]
        # Copies of edges and cover for the 2 recursive calls
        edges_for_u = dict(edges)
        edges_for_v = dict(edges)

        cover_for_u = set(cover)
        cover_for_v = set(cover)

        # deleting u and incident edges
        keys = list(edges_for_u.keys())
        cover_for_u.add(u)
        for key in keys:
            if u in key:
                del edges_for_u[key]

        a = bounded_tree_search_vertex_cover(edges_for_u, k-1, cover_for_u)
        
        # deleting v and incident edges
        keys = list(edges_for_v.keys())
        cover_for_v.add(v)
        for key in keys:
            if v in key:
                del edges_for_v[key]

        b = bounded_tree_search_vertex_cover(edges_for_v, k-1, cover_for_v)

        return a or b
# ==============================================================================

#print(bounded_tree_search_vertex_cover(G.get_edges(), 6, set()))
