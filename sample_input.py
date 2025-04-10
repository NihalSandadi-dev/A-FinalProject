import matplotlib.pyplot as plt
import numpy as np



"""
Sample Graph: Adjacency List Representation

sample_graph[0] = List for Node 0
Tuple (x, y) : x is the node and y is the edge weight

Node coordinates:
Node 0: [0, 4]
Node 1: [3, 2]
Node 2: [1, 1]
Node 3: [3, 0]
Node 4: [-2, 1]
"""

# Node coordinates
node_coords = {
    0: [0, 4],
    1: [3, 2],
    2: [1, 1],
    3: [3, 0],
    4: [-2, 1]
}

sample_graph = [
    [(1, 3), (2, 2), (4, 4)],
    [(0, 3), (2, 8)],
    [(0, 2), (1, 8), (3, 1)],
    [(2, 1), (4, 3)],
    [(0, 4), (3, 3)]
]

# Print adjacency lists
for i in range(len(sample_graph)):
    print("Adj List for Node: " + str(i) + " is: " + str(sample_graph[i]))

# For graph visualization 
plt.figure(figsize=(10, 8))

for node, coords in node_coords.items():
    plt.scatter(coords[0], coords[1], s=100, label=f'Node {node}')
    plt.annotate(f'Node {node}', (coords[0], coords[1]), xytext=(5, 5), textcoords='offset points')

for node in range(len(sample_graph)):
    for neighbor, weight in sample_graph[node]:
        if node < neighbor:
            start = node_coords[node]
            end = node_coords[neighbor]
            plt.plot([start[0], end[0]], [start[1], end[1]], 'b-', alpha=0.5)

            # Adding weight label at the middle of the edge
            mid_x = (start[0] + end[0]) / 2
            mid_y = (start[1] + end[1]) / 2
            plt.annotate(f'w={weight}', (mid_x, mid_y), xytext=(0, 5), textcoords='offset points', ha='center')

plt.grid(True)
plt.title('Graph Visualization')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.axis('equal')
# plt.show()
plt.savefig("sample_graph_plot")