input = "day5.txt"

counter = 0

with open(input) as f:
    lines = [x.strip() for x in f.readlines()]

ranges = lines[:lines.index("")]
ingredients = [int(x) for x in lines[lines.index("")+1:]]

for i in range(len(ranges)):
    ranges[i] = [int(x) for x in ranges[i].split("-")]

for i in ingredients:
    for j in range(len(ranges)):
        start = ranges[j][0]
        end = ranges[j][1]
        if start <= i <= end:
            counter += 1
            break

print(counter)