""" Minimum Spanning Tree using Kruskal's and Prim's Algorithm """
from collections import defaultdict
import heapq

class Graph:

    def __init__(self, v):
        self.vertices = v
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u,v,w])
    
    # find and union are used to quickly find whether including an edge will
    # form a cycle or not.
    def find(self, parent, i):
        """ find using path compression """
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, i, j):
        """ union by rank """
        x = self.find(parent, i)
        y = self.find(parent, j)
        
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[y] < rank[x]:
            parent[y] = x
        else:
            parent[y] = x
            rank[y] += 1

    def kruskal(self):
        """ Kruskal's Algorithm to find the MST """
        result = []

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = [i for i in range(self.vertices)]
        ranks = [0]*self.vertices
        
        # i for edges, e for mst
        i = e = 0

        while e < self.vertices - 1:
            u,v,w = self.graph[i]
            i += 1
            
            x = self.find(parent, u)
            y = self.find(parent, v)
            
            if x != y:
                e += 1
                result.append([u,v,w])
                self.union(parent, ranks, x, y)
        print(result)


G = Graph(4)
G.add_edge(0, 1, 10)
G.add_edge(0, 2, 6)
G.add_edge(0, 3, 5)
G.add_edge(1, 3, 15)
G.add_edge(2, 3, 4)
G.kruskal()


d = {0: [1,7], 1:[0, 2,7], 2:[1,3,5,8], 3:[2,4,5], 4:[3,5], 5:[2,3,4,6], 6:[5,7,8], 7:[0,1,6,8], 8:[2,6,7]}
w = {(0,1): 4, (0,7): 8, (1,2):8, (1,7):11, (2,3):7,(2,5):4,(2,8):2,(3,4):9,(3,5):14,(4,5):10,(5,6):2,(6,7):1,(6,8):6,(7,8):7}

## =============================================================================
## Prim's Algorithm
class MinHeap:
    """ A min-heap to use in prim's algorithm """
    def __init__(self, h):
        self.heap = h           # prototype -> [(dist1, node1), (dist2, node2)..]
        self.heap_size = len(h)
        self.pos = {h[i][1]:i for i in range(len(h))}

    def left(self, i):
        return 2*i+1

    def right(self, i):
        return 2*i+2

    def parent(self, i):
        return i//2

    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)

        if l < self.heap_size and self.heap[l][0] < self.heap[i][0]:
            smallest = l
        else: smallest = i
        
        if r < self.heap_size and self.heap[r][0] < self.heap[smallest][0]:
            smallest = r

        if smallest != i:
            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
            self.pos[self.heap[smallest][1]] = smallest
            self.pos[self.heap[i][1]] = i
            self.min_heapify(smallest)

    def build_min_heap(self):
        self.heap_size = len(self.heap)
        for i in range(len(self.heap)//2+1, -1, -1):
            self.min_heapify(i)

    def extract_min(self):
        if self.heap_size < 1:
            raise "Heap is Empty!"

        mini = self.heap[0]
        self.heap[0], self.heap[self.heap_size-1] = self.heap[self.heap_size-1], self.heap[0]
        self.pos[self.heap[0][1]] = 0
        self.pos[self.heap[self.heap_size-1][1]] = self.heap_size-1
        self.heap_size -= 1
        self.min_heapify(0)
        return mini

    def decrease_key(self, i, key):
        if self.heap[i][0] < key:
            return False
        self.heap[i][0] = key
        #print(self.heap[self.parent(i)], self.heap[i])
        while i >= 0 and self.heap[i][0] < self.heap[self.parent(i)][0]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            self.pos[self.heap[i][1]] = i
            self.pos[self.heap[self.parent(i)][1]] = self.parent(i)
            i = self.parent(i)
        return True
    
    def insert_key(self, dist, node):
        if self.heap_size < len(self.heap):
            self.heap[self.heap_size] = [float('inf'), node]
        else:
            self.heap.append([float('inf'), node])
        self.heap_size += 1
        self.pos[node] = self.heap_size-1
        self.decrease_key(self.heap_size-1, dist)

    def find_key(self, key):
        return self.pos.get(key, -1)

    def is_empty(self):
        return self.heap_size == 0


def prim(d,w,s):
    """ Prim's algorithm to find the minimum spanning tree. """
    heap = MinHeap([[0, s]])

    dist = [float('inf')]*len(d)
    visited = set()
    dist[s] = 0

    while not heap.is_empty():
        dis, u = heap.extract_min()

        visited.add(u)
        for v in d[u]:
            if v not in visited:
                if dist[v] > w[min(u,v), max(u,v)]:
                    dist[v] = w[min(u,v), max(u,v)]
                    pos = heap.find_key(v)
                    if pos != -1:
                        heap.decrease_key(pos, dist[v])
                    else:
                        heap.insert_key(dist[v], v)
    print(dist)
prim(d,w,0)
## =============================================================================
