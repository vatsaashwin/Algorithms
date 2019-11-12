from collections import defaultdict

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

		if rx == ry:
			return

		if rx > ry:
			parent[ry] = rx

		else:
			parent[rx] = ry
			if rx == ry:
				ry = ry+1
			
			dist = dist + wt
			output.append((x, y))

		if len(output) == n-1:
			return dist, output

	return dist, output

class PriorityQueue():
    def swap_node_idxs_in_map(self, n_1, n_2):
        temp = self.node_to_idx[n_1]
        self.node_to_idx[n_1] = self.node_to_idx[n_2]
        self.node_to_idx[n_2] = temp
        
    def swap(self, i, j):
        temp = self.H[i]
        self.H[i] = self.H[j]
        self.H[j] = temp
        self.swap_node_idxs_in_map(self.H[i][0], self.H[j][0])
        
    def min_heapify(self, i):
        l = 2*i + 1
        r = 2*i + 2
        least = i
        
        if(l<self.heap_size and self.H[l][1]<self.H[least][1]):
            least = l
        
        if(r<self.heap_size and self.H[r][1]<self.H[least][1]):
            least = r
            
        if(least != i):
            self.swap(i, least)
            self.min_heapify(least)
        return    
        
    def build_heap(self):
        for i in reversed(range(self.heap_size//2)):
            self.min_heapify(i)
    
    def extract_min(self):
        self.swap(0, self.heap_size-1)
        self.heap_size -= 1
        self.min_heapify(0)
        return self.H[self.heap_size][0]
    
    def decrease_key(self, v, updated_key):
        i = self.node_to_idx[v]
        self.H[i] = (v, updated_key)
        
        p = (i-1)//2
        while(p>=0 and self.H[i][1]<self.H[p][1]):
            self.swap(i, p)
            i = p
            p = (i-1)//2   
            
    def __init__(self, keys_dict):
        self.node_to_idx = dict()
        self.heap_size = len(keys_dict)
        self.H = []
        
        i=0
        for n in keys_dict:
            self.H.append((n, keys_dict[n]))
            self.node_to_idx[n] = i
            i += 1
            
        self.build_heap()


def MST_Prim(G):
    r = 'a'
    adj_list = defaultdict(lambda:[])
    edge_weights = defaultdict(lambda:float("infinity"))
    
    for tup in G:
        adj_list[tup[0]].append(tup[1])
        adj_list[tup[1]].append(tup[0])
        edge_weights[(tup[0], tup[1])] = tup[2]
        edge_weights[(tup[1], tup[0])] = tup[2]
        
    keys_dict = defaultdict(lambda: float("infinity"))
    ancestor = defaultdict(lambda:None)
    node_in_Q = dict()
    
    for n in adj_list:
        keys_dict[n] = float("infinity")
        ancestor[n] = None
        node_in_Q[n] = 1
    
    keys_dict[r] = 0
    Q = PriorityQueue(keys_dict)
    A = []
    mst_cost = 0
    
    while(Q.heap_size != 0):
        u = Q.extract_min()
        node_in_Q[u] = 0

        for v in adj_list[u]:
            if(node_in_Q[v] and edge_weights[(u, v)]<keys_dict[v]):
                ancestor[v] = u
                keys_dict[v] = edge_weights[(u, v)]
                Q.decrease_key(v, edge_weights[(u, v)])
        
        if(ancestor[u] != None):
            A.append((ancestor[u], u))
            mst_cost += edge_weights[(ancestor[u], u)]
    
    return (mst_cost, A)


G = ([(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])

print(MST_Kruskel(G))
print(MST_Prim(G))