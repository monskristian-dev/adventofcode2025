import numpy as np

def merge_connected_checkpoints(checkpoint_rows):

    parent_map = {}

    def find_root(node):
        if node not in parent_map:
            parent_map[node] = node
            return node
        if parent_map[node] != node:
            parent_map[node] = find_root(parent_map[node])
        return parent_map[node]

    def union(node_a, node_b):
        root_a = find_root(node_a)
        root_b = find_root(node_b)
        if root_a != root_b:
            parent_map[root_b] = root_a

    for row in checkpoint_rows:
        if not row: continue
        row_representative = row[0]
        for value in row[1:]:
            union(row_representative, value)

    grouped_checkpoints = {}
    
    for value in parent_map:
        root = find_root(value)
        if root not in grouped_checkpoints:
            grouped_checkpoints[root] = []
        grouped_checkpoints[root].append(value)
        
    return [sorted(group) for group in grouped_checkpoints.values()]

def distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)**0.5

input_file = "day8.txt"

pair_list = []

with open(input_file) as f:
    lines = [[int(x) for x in line.split(",")] for line in f]

data_array = np.zeros((len(lines), len(lines)))

for i in range(len(lines)):
    for j in range(len(lines)):
        if i == j:
            data_array[i][j] = np.nan
        else:
            data_array[i][j] = distance(lines[i], lines[j])

flat_index = np.nanargmin(data_array)
row, col = np.unravel_index(flat_index, data_array.shape)
data_array[row][col] = np.nan
data_array[col][row] = np.nan
pair_list.append([int(row), int(col)])
box_length = [len(x) for x in merge_connected_checkpoints(pair_list)]

while box_length[0] != 1000:
    flat_index = np.nanargmin(data_array)
    row, col = np.unravel_index(flat_index, data_array.shape)
    data_array[row][col] = np.nan
    data_array[col][row] = np.nan
    pair_list.append([int(row), int(col)])
    box_length = [len(x) for x in merge_connected_checkpoints(pair_list)]

print (lines[row][0]*lines[col][0])