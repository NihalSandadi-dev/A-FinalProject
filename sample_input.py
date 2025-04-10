# Sample Graph: Adjacency List Representation

# sample_graph[0] = List for Node 0
# Tuple (x, y) : x is the node and y is the edge weight
sample_graph = [
    [(1, 3), (2, 2), (4, 4)],
    [(0, 3), (2, 8)],
    [(0, 2), (1, 8), (3, 1)],
    [(2, 1), (4, 3)],
    [(0, 4), (3, 3)]
]

for i in range(len(sample_graph)):
    print("Adj List for Node: " + str(i) + " is: " + str(sample_graph[i]))