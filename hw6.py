from collections import defaultdict
from heapq import heappush, heappop, heapify

def sortElement(index):
    return index[2]

def find(parent, x):
	while parent[x] != -1:
		x = parent[x]
	return x

def makeSet(Graph):
	edge_List= []
	v_list = set()
	for (u, v, wt) in Graph:
		edge_List.append((u, v, wt))
		v_list.add(u)
		v_list.add(v)
	return edge_List, v_list

def MST_Kruskel(Graph):
	parent = defaultdict(lambda:-1)
	#makeSet from input graph
	edge_List, v_list = makeSet(Graph)
	n = len(v_list)

	#sort the edges by length
	edge_List.sort(key=sortElement)

	output = []
	dist = 0

	#union
	for (x, y, wt) in edge_List:

		rx = find(parent, x)
		ry = find(parent, y)

		# if rx == ry:
		# 	return

		if rx != ry:	
			parent[rx] = ry
			dist = dist + wt
			output.append((x, y))

		if len(output) == n-1:
			return dist, output

	return dist, output

def decreaseKey(Queue, v, key):
    for i, (val, node) in enumerate(Queue):
        if node == v:
            Queue[i], (key, node) = (key, node), Queue[i]
            heapify(Queue)

def MST_Prim(Graph):
    edge_List = defaultdict(list)
    output = []
    cost = {}
    prev = defaultdict(lambda: -1)
    visited = set()

    for (u, v, wt) in Graph:
        edge_List[u].append((v, wt))
        edge_List[v].append((u, wt))
        if u not in cost:
        	cost[u] = float('inf')
        	prev[u] = None
        if v not in cost:
        	cost[v] = float('inf')
        	prev[v] = None

    Queue = []
    cost[0], wt = 0, 0

    for v, val in cost.items():
        heappush(Queue, (val, v))

    while Queue:
        #DeleteMin
        vx = heappop(Queue)
        #collection of visited nodes
        x= vx[1]
        visited.add(x)

        for (i, j) in edge_List[x]:
            if i not in visited and cost[i] > j:
                cost[i] = j
                prev[i] = x
                decreaseKey(Queue, i, cost[i])

    #print output
    for u, v in prev.items():
        if v is not None and u is not None:
            output.append((v, u))
            wt = wt + cost[u]
    return wt, output

G =  [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)]

print(MST_Kruskel(G))
print(MST_Prim(G))


import numpy as np
import matplotlib.pyplot as plt

t = [315745,140359,49370,19607,4994]
plt.xticks(t)
# t = [4994,19607,49370,140359,315745]
#time(in secs) from server
MST_prim = [0.441,0.435,0.495,0.116,0.202]
# MST_prim = [0.202, 0.116, 0.495,0.435,0.441]
MST_kruskel = [1.538,2.547,3.977,0.963,1.419]
# MST_kruskel = [1.419, 0.963, 3.977, 2.547, 1.538]

g1, = plt.plot(t, MST_prim, label="MST_Prim",  marker='o')
g2, = plt.plot(t, MST_kruskel, label="MST_Kruskel",  marker='o')

plt.legend()
plt.xlabel('Number of Edges')
plt.ylabel('Running Time (sec)')
plt.show()
