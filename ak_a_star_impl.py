from collections import deque
import heapq
from helper_functions import calculate_euclidean_distance
from helper_functions import PriorityNode
from sample_input import node_coords, sample_graph

def a_star(graph, node_coordinates, start, end):
    # if start is the end
    if start == end:
        return 0, [start]
    
    # heap for nodes to be evaluated
    # using a priority queue with (f_score, node) tuples
    curr_heap = []
    
    # g_score is cost from start to current node
    # infinity for all nodes except start
    g_score = {node: float('inf') for node in range(len(graph))}
    g_score[start] = 0
    
    # f_score: g_score + heuristic
    # infinity by default for all nodes except start
    f_score = {node: float('inf') for node in range(len(graph))}
    f_score[start] = calculate_euclidean_distance(node_coordinates[start], node_coordinates[end])
    
    heapq.heappush(curr_heap, (f_score[start], start))
    
    # for path reconstruction
    successor = {}
    
    # set of nodes already evaluated
    visited = set()
    
    while curr_heap:
        current_f, current = heapq.heappop(curr_heap)
        if current in visited:
            continue

        if current == end:
            path = []
            while current in successor:
                path.append(current)
                current = successor[current]
            path.append(start)
            path.reverse()
            return g_score[end], path
        
        visited.add(current)
        
        for neighbor, weight in graph[current]:
            if neighbor in visited:
                continue
            
            tentative_g_score = g_score[current] + weight
            
            if tentative_g_score < g_score[neighbor]:
                successor[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + calculate_euclidean_distance(node_coordinates[neighbor], node_coordinates[end])
                
                heapq.heappush(curr_heap, (f_score[neighbor], neighbor))
    
    # No path found
    return float('inf'), []

test_start = 1
test_end = 4
# res_paths = a_star(node_coords, sample_graph, test_start, test_end)
res_paths = a_star(sample_graph, node_coords, test_start, test_end)
print(res_paths)


# PrioityNode Class Test
# h = []
# heapq.heappush(h, PriorityNode("A", 5))
# heapq.heappush(h, PriorityNode("B", 3))
# heapq.heappush(h, PriorityNode("C", 7))
# heapq.heappush(h, PriorityNode("D", 11))
# heapq.heappush(h, PriorityNode("E", 2))

# while h:
#     node = heapq.heappop(h)
#     print("Popped node key: " + node.key + " and value: " + str(node.priority))