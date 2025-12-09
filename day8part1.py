import numpy as np

input_file = "day8.txt"

pair_list = []
connections = 1000

def distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)**0.5

def merge_common_lists(list_of_lists):
    pool = []
    for row in list_of_lists:
        current_set = set(row)
        merged_set = current_set
        remaining_pool = []
        for existing_set in pool:
            if not existing_set.isdisjoint(merged_set):
                merged_set.update(existing_set)
            else:
                remaining_pool.append(existing_set)
        pool = remaining_pool + [merged_set]
    return [sorted(list(s)) for s in pool]

with open(input_file) as f:
    lines = [[int(x) for x in line.split(",")] for line in f]

data_array = np.zeros((len(lines), len(lines)))

for i in range(len(lines)):
    for j in range(len(lines)):
        if i == j:
            data_array[i][j] = np.nan
        else:
            data_array[i][j] = distance(lines[i], lines[j])

for i in range(connections):
    flat_index = np.nanargmin(data_array)
    row, col = np.unravel_index(flat_index, data_array.shape)
    data_array[row][col] = np.nan
    data_array[col][row] = np.nan
    pair_list.append([int(row), int(col)])

box_length = [len(x) for x in merge_common_lists(pair_list)]
box_length.sort()

print (np.prod(box_length[-3:]))