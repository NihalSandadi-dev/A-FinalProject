import numpy as np
import matplotlib.pyplot as plt
import random
import math
from helper_functions import calculate_euclidean_distance

def generate_random_coordinates(num_nodes, x_range=(-10, 10), y_range=(-10, 10)):
    # generate random coordinates for the specified number of nodes
    node_coords = {}
    for i in range(num_nodes):
        x = random.uniform(x_range[0], x_range[1])
        y = random.uniform(y_range[0], y_range[1])
        node_coords[i] = [round(x, 2), round(y, 2)]
    return node_coords

# edge probability could help test runtime for dense vs sparse graphs
# weight_type: 'unit' (all weights = 1), 'random', or 'euclidean'
# weight_range: range for random weights (min, max)
def generate_graph(num_nodes, edge_probability=0.3, weight_type='euclidean', 
                  weight_range=(1, 10), node_coords=None, visualize=False, save_path=None):
    # Generate node coordinates if not provided
    if node_coords is None:
        node_coords = generate_random_coordinates(num_nodes)
    
    # Create adjacency list
    adj_list = [[] for _ in range(num_nodes)]
    
    # Generate edges
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j and random.random() < edge_probability:
                if weight_type == 'unit':
                    weight = 1
                elif weight_type == 'random':
                    weight = round(random.uniform(weight_range[0], weight_range[1]), 2)
                elif weight_type == 'euclidean':
                    weight = calculate_euclidean_distance(node_coords[i], node_coords[j])
                
                adj_list[i].append((j, weight))
    
    if visualize:
        visualize_graph(adj_list, node_coords, save_path)
    
    return adj_list, node_coords

# generate graph visalization
def visualize_graph(adj_list, node_coords, save_path=None):
    plt.figure(figsize=(12, 10))
    
    for node, coords in node_coords.items():
        plt.scatter(coords[0], coords[1], s=100)
        plt.annotate(f'{node}', (coords[0], coords[1]), xytext=(5, 5), 
                    textcoords='offset points')
    
    for node in range(len(adj_list)):
        for neighbor, weight in adj_list[node]:
            if node < neighbor:
                start = node_coords[node]
                end = node_coords[neighbor]
                plt.plot([start[0], end[0]], [start[1], end[1]], 'b-', alpha=0.5)
                mid_x = (start[0] + end[0]) / 2
                mid_y = (start[1] + end[1]) / 2
                plt.annotate(f'{weight:.2f}', (mid_x, mid_y), xytext=(0, 5), 
                            textcoords='offset points', ha='center')
    
    plt.grid(True)
    plt.title(f'graph with {len(node_coords)} nodes')
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.axis('equal')
    
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
    
    plt.close()

def print_graph_info(adj_list, node_coords):
    print(f"graph with {len(adj_list)} nodes")
    print("\nnode coordinates:")
    for node, coords in node_coords.items():
        print(f"node {node}: {coords}")
    
    print("\nadjacency lists:")
    for i in range(len(adj_list)):
        print(f"adj List for Node {i}: {adj_list[i]}")

# testing if it works as intended
if __name__ == "__main__":
    # input params:
    # num_nodes
    # edge_probability
    # weight_type
    # weight_range
    # node_coords
    # visualize
    # save_path
    
    seed_value = 67
    random.seed(seed_value)
    np.random.seed(seed_value)


    # small graph with unit weights
    print("generating small graph with unit weights...")
    small_unit_adj_list, small_unit_coords = generate_graph(
        num_nodes=5,
        edge_probability=0.7, 
        weight_type='unit',
        weight_range=(1, 10),
        node_coords=None,
        visualize=True,
        save_path="small_unit_graph.png"
    )
    print_graph_info(small_unit_adj_list, small_unit_coords)

    # large graph with random weights
    # print("generating large graph with random weights...")
    # large_random_adj_list, large_random_coords = generate_graph(
    #     num_nodes=50,
    #     edge_probability=0.3, 
    #     weight_type='random',
    #     weight_range=(1, 50),
    #     node_coords=None,
    #     visualize=True,
    #     save_path="large_random_graph.png"
    # )
    # print_graph_info(large_random_adj_list, large_random_coords)