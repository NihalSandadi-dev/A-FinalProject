from queue import PriorityQueue
import random
import numpy as np
from input_generator import generate_graph, print_graph_info

def dijkstra(start, goal, adj_list):
    """Dijkstra's algorithm for finding the shortest path using numeric node IDs."""
    num_nodes = len(adj_list)
    priority_queue = PriorityQueue()
    priority_queue.put((0, start))
    
    came_from = {}  # For path reconstruction
    cost_so_far = {node: float('inf') for node in range(num_nodes)}
    cost_so_far[start] = 0

    while not priority_queue.empty():
        current_cost, current = priority_queue.get()

        # Reconstruct path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return cost_so_far[goal], path[::-1]

        for neighbor, weight in adj_list[current]:
            new_cost = cost_so_far[current] + weight
            
            if new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current
                priority_queue.put((new_cost, neighbor))

    return float('inf'), []

if __name__ == "__main__":
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

    print_graph_info(adj_list, node_coords)

    test_start = 1
    test_goal = 4
    cost, path = dijkstra(test_start, test_goal, adj_list)
    
    print(f"\nDijkstra Result from node {test_start} to {test_goal}:")
    print(f"Total Cost: {cost}")
    print(f"Path: {path}")