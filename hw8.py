import heapq
import random
from collections import defaultdict


#functions for heap operations
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return


def percolateUp(arr, node):
    parent = int((node - 1) / 2)
    if parent <= 0:
        return
    if arr[node] > arr[parent]:
        swap(arr, node, parent)
    else:
        percolateUp(arr, parent)


def push(arr, val):
    arr.append(val)
    percolateUp(arr, len(arr) - 1)
    return


def percolateDown(arr, node):
    arrlen = len(arr) - 1
    child = 2 * node + 1
    if child > arrlen:
        return
    if (child + 1 <= arrlen) and (arr[child + 1] > arr[child]):
        child += 1
    if arr[node] < arr[child]:
        swap(arr, node, child)
        percolateDown(arr, child)
    else:
        return


def pop(arr):
    arrlen = len(arr) - 1
    swap(arr, 0, arrlen)
    max = arr.pop(arrlen)
    percolateDown(arr, 0)
    return max


def heapify(arr):
    arrlen = len(arr) - 1
    for n in range(int(arrlen / 2), -1, -1):
        percolateDown(arr, n)
    return


#main functions


def backTrace(V, G):
    for x, cnt in enumerate(G):
        if (cnt[0] == V):
            return cnt[1]
    return 0


def findNode(V, H):
    cnt = 0
    for i in H:
        if i[1] == V:
            return cnt
        cnt = cnt + 1
    return -1


def augmentGraph(sink, Min_Flow, path, G):
    i = 0
    result = []
    while i < len(path):

        if path[i] == sink:
            break

        v_temp = []
        temp = []
        u = path[i]
        v = path[i + 1]

        v_temp = [z for z in G[u] if z[1] != v]
        temp = [z for z in G[u] if z[1] == v]
        if temp[0][2] - Min_Flow > 0:
            temp.append((u, v, temp[0][2] - Min_Flow, temp[0][3] + Min_Flow))
        result.append((u, v, Min_Flow))
        G[u] = v_temp

        v_temp = []
        temp = []

        v_temp = [z for z in G[v] if z[1] != u]
        temp = [z for z in G[v] if z[1] == u]
        if temp != []:
            v_temp.append((v, u, temp[0][2] + Min_Flow, temp[0][3] - Min_Flow))
        else:
            v_temp.append((v, u, Min_Flow, 0))
        G[v] = v_temp

        i = i + 1

    return result


def maxSpanningTree(source, sink, G, V):
    v_list = defaultdict(lambda: -1)
    max_heap = []

    for v in V:
        key, u, parent = V[v]
        v_list[u] = (key, u, parent)

    v_list[source] = (0, source, -1)

    for v in v_list:
        push(max_heap, v_list[v])

    heapify(max_heap)
    visited = set()

    while (v_list[sink][2] == -1 and len(max_heap) > 0):
        (a, Vertex, b) = pop(max_heap)
        visited.add(Vertex)
        for u, v, cap, interim_flow in G[Vertex]:
            if v in visited:
                continue
            if v_list[sink][2] != -1:
                break

            x = findNode(v, max_heap)
            key = max_heap[x][0]

            if cap > 0 and cap > key and v not in visited:
                max_heap[x] = (cap, v, Vertex)
                v_list[v] = (cap, v, Vertex)
        heapify(max_heap)

    (Min_Flow, path) = findMinFlow(sink, v_list, G)
    return (Min_Flow, path)


def Max_Flow_Fat(source, sink, G):
    # initialise graph
    output = []
    INF = 999999999
    Max_Flow = 0
    cnt = 0

    V = defaultdict(list)
    Graph = defaultdict(list)
    for start, end, cap in G:
        V[start] = (-INF, start, -1)
        V[end] = (-INF, end, -1)
        Graph[start].append((start, end, cap, 0))

    # for Max_Flow
    while (cnt < len(V)):
        Min_Flow, path = maxSpanningTree(source, sink, Graph, V)

        if Min_Flow <= 0:
            break

        if path == [] or path[0] != sink or path == None:
            break

        path.reverse()
        olist = augmentGraph(sink, Min_Flow, path, Graph)
        output.extend(olist)
        Max_Flow += Min_Flow
        cnt += 1

    return (Max_Flow, output)


def checkPath(source, sink, V, G):
    Q = []

    path = defaultdict(list)
    path[source] = 0
    visited = [0] * (len(V))
    visited[source] = 1

    Q.append(V[source])

    while Q:
        u, p = Q.pop()
        for i, x in enumerate(G[u]):
            if visited[x[0]] == 0 and x[1] > 0:
                V[x[0]] = (x[0], u)
                Q.append(V[x[0]])
                visited[x[0]] = 1
    return (1) if visited[sink] else (0)


def findMinFlow(sink, V, G):
    res = []
    Min_Flow = 0
    cnt = 0

    if res != [] and res[0] != sink:
        return (Min_Flow, [])

    dest = sink
    while (cnt < len(V)):
        (cap, vertex, parent) = V[dest]
        if parent == -1:
            break

        for u, v, c, f in G[parent]:
            if (v == vertex and dest == sink):
                cap = c
                Min_Flow = c
                break

        if (dest == sink):
            res.append(dest)
        if (parent != -1):
            res.append(parent)
        if (Min_Flow > cap):
            Min_Flow = cap
        dest = parent

        cnt += 1

    return (Min_Flow, res)


def Max_Flow_Short(source, sink, Graph):
    # initialise graphs
    G = defaultdict(list)
    resGraph = defaultdict(list)
    V = defaultdict(list)

    parent = -1

    for initial, end, cap in Graph:
        G[initial].append((end, cap))
        G[end].append((initial, 0))
        resGraph[initial].append((end, 0))
        V[initial] = (initial, parent)
        V[end] = (end, parent)

    Max_Flow = 0
    result = []
    while True:
        flow = 9999999999
        visited = checkPath(source, sink, V, G)
        if visited == 0:
            break
        node = sink

        while node != source:
            current, parent = V[node]
            current_flow = backTrace(current, G[parent])
            flow = min(flow, current_flow)
            node = parent
        Max_Flow += flow
        node = sink

        while (node != source):
            v, u = V[node]
            v_temp = []
            temp = []
            v_temp = [x for x in G[u] if x[0] != v]
            temp = [x for x in G[u] if x[0] == v]
            v_temp.append((v, temp[0][1] - flow))
            result.append((u, v, flow))
            G[u] = v_temp

            v_temp = []
            temp = []
            v_temp = [z for z in G[v] if z[0] != u]
            temp = [z for z in G[v] if z[0] == u]
            v_temp.append((u, temp[0][1] + flow))
            G[v] = v_temp

            node = u
    return (Max_Flow, result)


# (8, [(0, 3, 6), (3, 4, 6), (0, 1, 2), (1, 4, 2)])
# (8, [(3, 4, 6), (0, 3, 6), (1, 4, 2), (0, 1, 2)])

# print(
#     Max_Flow_Fat(0, 4, [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5),
#                         (2, 4, 7), (3, 4, 9)]))

# print(
#     Max_Flow_Short(0, 4, [(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8),
#                           (1, 4, 5), (2, 4, 7), (3, 4, 9)]))
