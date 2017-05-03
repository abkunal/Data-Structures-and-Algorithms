""" Minimum Cut problem by Karger's Algorithm """

import random
import copy

class Graph:
    
    def __init__(self):
        self.adj_list = {}
        self.min_cut = float('inf')

    def karger(self):
        # deepcopying to prevent adj_list from changing
        dup = copy.deepcopy(self.adj_list)

        # while more than 2 vertices are left
        while len(dup) > 2:
            # pick an edge randomly (its not uniformly random but should be)
            v1 = random.choice(list(dup.keys()))
            v2 = random.choice(dup[v1])
            
            # contract edges into one edge
            dup[v1].extend(dup[v2])
            for ver in dup[v2]:
                dup[ver].remove(v2)
                dup[ver].append(v1)
            
            # remove self loops
            while v1 in dup[v1]:
                dup[v1].remove(v1)

            del dup[v2]
        
        p = dup.popitem()
        if len(p[1]) < self.min_cut:
            self.min_cut = len(p[1])

    def find_min_cut(self):
        # run karger many times to make sure we get the minimum cut
        for i in range(len(self.adj_list)):
            self.karger()
        print(self.min_cut)

G = Graph()
G.adj_list[1] = [2,4]
G.adj_list[2] = [1,3,4]
G.adj_list[3] = [2,4]
G.adj_list[4] = [1,2,3]

G.find_min_cut()
