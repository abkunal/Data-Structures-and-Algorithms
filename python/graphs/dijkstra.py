""" Dijkstra's Algorithm for finding shortest path from a single source """

import heapq

def dijkstra(d, w, s):
	""" Returns the list of shortest distances from vertex s 
		
		d: adjacency list {0: [1,2,3,...], 1: [3,4,5,...], ....}
		w: edge weights {(start, end): weight}
		s: the vertex to start from
	"""
	# initialize our minheap
	minheap = []
	# initially all distance are infinity
	distance = [float('inf') for i in range(len(d))]
	distance[s] = 0

	# set of visited vertices
	visited = set()
	# push s into the minheap
	heapq.heappush(minheap, (distance[s], s))

	# while minheap is not empty
	while minheap:
		# pop the vertex with the shortest distance
		dist, u = heapq.heappop(minheap)

		# add it to visited set
		visited.add(u)

		# for every neighbour v of u
		for v in d[u]:
			# v is not visited yet
			if v not in visited:
				# if distance to v is greater than distance to u + weight of edge (u,v)
				# update distance to v
				if distance[v] > dist + w[(u, v)]:
					distance[v]  = dist + w[(u, v)]
					heapq.heappush(minheap, (distance[v], v))
	return distance

d = {0: [1,2], 1:[2,3], 2:[1,3,4], 3:[4], 4:[0,3]}
w = {(0,1): 10, (0,2):5, (1,2):2, (1,3):1, (2,1):3, (2,3):9,(2,4):2, (3,4):4, (4,0):7, (4,3):6}

print(dijkstra(d,w,0))