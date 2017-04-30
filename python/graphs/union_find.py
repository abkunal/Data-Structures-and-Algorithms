""" Union-Find Algorithm to find cycles in a graph """

from collections import defaultdict

class Graph:
    
    def __init__(self, v):
        self.vertices = v       # no. of vertices in the graph
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def find(self, parent, i):
        if parent[i] == -1:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, i, j):
        x = self.find(parent, i)
        y = self.find(parent, j)
        parent[x] = y
    
    def is_cyclic(self):
        """ Returns True if the graoh contains a cycle """
        parent = [-1]*self.vertices

        for i in self.adj_list:
            for j in self.adj_list[i]:
                x = self.find(parent, i)
                y = self.find(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)
        return False
    

    def find_path_compression(self, parent, i):
        """ Find using path compression """
        if parent[i] == i:
            return i
        return self.find_path_compression(parent, parent[i])

    def union_using_rank(self, parent, rank, i, j):
        xroot = self.find_path_compression(parent, i)
        yroot = self.find_path_compression(parent, j)

        if rank[xroot] < rank[yroot]:
            parent[xroot]= yroot
        elif rank[yroot] < rank[xroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1


G = Graph(4)
G.add_edge(0,1)
G.add_edge(1,2)
G.add_edge(3,2)
print(G.is_cyclic())
