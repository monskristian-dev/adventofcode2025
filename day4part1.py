input = "day4.txt"
map_data = []
count = 0

with open(input) as f:
    raw_data = [x.strip() for x in f.readlines()]

for i in range(len(raw_data)):
    raw_data[i] = raw_data[i].replace(".","0")
    raw_data[i] = raw_data[i].replace("@","1")
    map_data.append([int(x) for x in list(raw_data[i])])

for i in range(len(map_data)):
    for j in range(len(map_data[i])):
        if map_data[i][j] == 1:
            indexN = i - 1
            indexW = j - 1
            indexS = i + 2
            indexE = j + 2
            indexN = indexN if indexN > 0 and indexN < len(map_data) else None
            indexW = indexW if indexW > 0 and indexW < len(map_data[i]) else None
            indexS = indexS if indexS > 0 and indexS < len(map_data) else None
            indexE = indexE if indexE > 0 and indexE < len(map_data[i]) else None
            window = [row[indexW:indexE] for row in map_data[indexN:indexS]]
            window_sum = sum([element for row in window for element in row]) - 1
            if window_sum < 4:
                count += 1
        else:
            pass

print (count)
