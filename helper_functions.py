from math import sqrt


def calculate_euclidean_disatance(start, end):
    x1, y1 = start
    x2, y2 = end
    return sqrt((x2-x1)**2 + (y2-y1)**2)