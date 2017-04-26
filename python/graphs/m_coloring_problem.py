""" 
    Given an undirected graph find whether the nodes can be colored with m 
    different colors with no two adjacent nodes having the same color.
"""

class UndirectedGraph:
    """ An undirected graph """
    
    # Node Class
    class Node:
        """ Represents a node/vertex in a graph """
        
        def __init__(self, val):
            self._val = val
            self._color = None

        def get_val(self):
            return self._val

        def get_color(self):
            return self._color

        def set_color(self, color):
            self._color = color

    def __init__(self):
        self._adj = {}

    def has_vertex(self, v):
        """ Returns True if graph contains the given vertex """
        for node in self._adj:
            if node.get_val() == v:
                return True
        return False

    def add_vertex(self, v):
        """ Adds the given vertex to the graph if not already present """
        if not self.has_vertex(v):
            self._adj[self.Node(v)] = {}
        return True
    
    def _get_vertex(self, v):
        """ Returns the requested vertex """
        for vertex in self._adj:
            if vertex.get_val() == v:
                return vertex
    
    def add_edge(self, start, end):
        """ Adds an edge between start and end if both vertices exists in graph. """
        if self.has_vertex(start) and self.has_vertex(end):
            #print(start, end)
            start = self._get_vertex(start)
            end = self._get_vertex(end)
            self._adj[start][end] = True
            self._adj[end][start] = True
            return True
        return False

    def remove_colors(self):
        """ Sets the colors of all the nodes in the graph to None """
        for node in self._adj:
            node.set_color(None)
        return True

    def color_graph(self, m):
        """ Returns True if the graph can be colored with m colors, False otherwise """
        vertices = list(self._adj.keys())
        return self._color_it(vertices, 0, len(vertices), m)

    def _can_color(self, v, color):
        """ Returns True if vertex v can be colored with the given color """
        # Check all the neighbour of v
        for u in self._adj[v]:
            if u.get_color() == color:
                return False
        return True

    def _color_it(self, vertices, colored, to_color, m):
        """ A backtracking algorithm to find whether the graph can be colored
            with m colors
            vertices: A list of vertices
            covered: the number of vertices colored so far
            to_color: the total number to vertices to color
            m: maximum number that can be used to color the graph

            Returns True if the graph can be colored with m colors, False otherwise
        """
        if colored >= to_color:
            return True
        else:
            for i in range(m):
                if self._can_color(vertices[colored], i):
                    vertices[colored].set_color(i)
                    if self._color_it(vertices, colored+1, to_color, m):
                        return True
                    vertices[colored].set_color(None)

        return False


G = UndirectedGraph()
G.add_vertex("A")
G.add_vertex("B")
G.add_vertex("C")
G.add_vertex("D")
G.add_vertex("E")
G.add_vertex("F")
G.add_vertex("G")
G.add_vertex("H")
G.add_vertex("I")
G.add_vertex("J")

G.add_edge("A", "B")
G.add_edge("A", "F")
G.add_edge("B", "C")
G.add_edge("B", "G")
G.add_edge("C", "D")
G.add_edge("C", "H")
G.add_edge("D", "E")
G.add_edge("D", "I")
G.add_edge("E", "A")
G.add_edge("E", "J")
G.add_edge("F", "H")
G.add_edge("F", "I")
G.add_edge("G", "J")
G.add_edge("G", "I")
G.add_edge("J", "H")

print(G.color_graph(4))


G = UndirectedGraph()
G.add_vertex("A")
G.add_vertex("B")
G.add_vertex("C")
G.add_vertex("D")

G.add_edge("A", "B")
G.add_edge("A", "C")
G.add_edge("B", "D")
G.add_edge("B", "C")
print(G.color_graph(2))
