from math import sqrt
import heapq

class PriorityNode:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

def calculate_euclidean_disatance(start, end):
    x1, y1 = start
    x2, y2 = end
    return sqrt((x2-x1)**2 + (y2-y1)**2)