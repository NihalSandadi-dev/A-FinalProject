import math
from queue import PriorityQueue

def dijkstra(start, goal, graph, edge_weights):
    """Dijkstra's algorithm for finding the shortest path."""
    priorityQueue = PriorityQueue()
    priorityQueue.put((0, start))  # Priority queue with (cost, node)
    came_from = {}  # Track the path
    graph_score = {node: float('inf') for node in graph}  # Start with infinite cost
    graph_score[start] = 0

    while not priorityQueue.empty():
        current_cost, current = priorityQueue.get()

        # if we reached the end
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor in graph[current]:
            # Calculate the cost to reach the neighbor
            temp_score = graph_score[current] + edge_weights[(current, neighbor)]

            if temp_score < graph_score[neighbor]:
                came_from[neighbor] = current
                graph_score[neighbor] = temp_score
                priorityQueue.put((temp_score, neighbor))

    return None

# Example input graph
graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'D'],
    'C': ['D', 'E'],
    'D': ['A', 'B', 'C'],
    'E': ['A', 'C']
}

positions = {
    'A': (0, 4),
    'B': (3, 2),
    'C': (3, 0),
    'D': (1, 1),
    'E': (-2, 1)
}

edge_weights = {
    ('A', 'B'): 3.61,
    ('A', 'D'): 3.16,
    ('A', 'E'): 3.61,
    ('B', 'D'): 2.24,
    ('C', 'D'): 2.24,
    ('C', 'E'): 5.10,
    ('B', 'A'): 3.61,
    ('D', 'A'): 3.16,
    ('E', 'A'): 3.61,
    ('D', 'B'): 2.24,
    ('D', 'C'): 2.24,
    ('E', 'C'): 5.10,
}

start = 'A'
goal = 'C'
path = dijkstra(start, goal, graph, edge_weights)

print(f"Path from {start} to {goal}: {path}")
