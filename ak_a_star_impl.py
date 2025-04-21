from collections import deque
import heapq
import random
import numpy as np
from helper_functions import calculate_euclidean_distance
from helper_functions import PriorityNode
from input_generator import generate_graph, print_graph_info

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

if __name__ == "__main__":
# Set the same seed as input_generator's test case for reproducibility
    seed_value = 67
    random.seed(seed_value)
    np.random.seed(seed_value)

    # Generate the small unit graph as in input_generator's test
    # adj_list, node_coords = generate_graph(
    #     num_nodes=5,
    #     edge_probability=0.7,
    #     weight_type='unit',
    #     visualize=True  # Set to True to visualize the graph
    # )

    # Generate the small unit graph as in input_generator's test
    adj_list, node_coords = generate_graph(
        num_nodes=50,
        edge_probability=0.3, 
        weight_type='random',
        weight_range=(1, 50),
        node_coords=None,
        visualize=True
        # save_path="large_random_graph.png"
    )

        

    # Print graph information for verification
    print_graph_info(adj_list, node_coords)

    # Test A* algorithm
    test_start = 1
    test_end = 4
    cost, path = a_star(adj_list, node_coords, test_start, test_end)
    
    print(f"\nA* Result from node {test_start} to {test_end}:")
    print(f"Cost: {cost}")
    print(f"Path: {path}")
