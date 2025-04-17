import math
from queue import PriorityQueue

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    
def a_star(start, goal, graph, edge_weights, positions):
    # priority queue to traverse the graph
    priorityQueue = PriorityQueue()
    priorityQueue.put((0, start))
    
    # used to remember the path
    path_traveled = {}
    
    # set distance to infinity
    graph_score = {node: float('inf') for node in graph}
    graph_score[start] = 0
    
    cost_score = {node: float('inf') for node in graph}
    cost_score[start] = calculate_distance(positions[start], positions[goal])
    
    # start pathfinding
    while not priorityQueue.empty():
        _, current = priorityQueue.get()
        
        # if we reached our goal
        if current == goal:
            path = []
            while current in path_traveled:
                path.append(current)
                current = path_traveled[current]
            path.append(start)
            return path[::-1]
        
        for neighbor in graph[current]:
            temp_score = graph_score[current] + edge_weights[(current, neighbor)]
            
            if temp_score < graph_score[neighbor]:
                path_traveled[neighbor] = current
                graph_score[neighbor] = temp_score
                cost_score[neighbor] = graph_score[neighbor] + calculate_distance(positions[neighbor], positions[goal])
                priorityQueue.put((cost_score[neighbor], neighbor))
                
    return None
        



# Example inputs
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

start = 'B'
goal = 'E'

path = a_star(start, goal, graph, edge_weights, positions)

print(f"Path from {start} to {goal}: {path}")