input_file = "day5.txt"

ranges = []
with open(input_file) as f:
    lines = [x.strip() for x in f.readlines() if x.strip()]

for line in lines:
    if "-" in line and line[0].isdigit():
        parts = line.split("-")
        start = int(parts[0])
        end = int(parts[1])
        ranges.append([start, end])

ranges.sort(key=lambda x: x[0])

merged_ranges = []

if ranges:
    curr_start, curr_end = ranges[0]
    for next_start, next_end in ranges[1:]:
        if next_start <= curr_end + 1: 
            curr_end = max(curr_end, next_end)
        else:
            merged_ranges.append((curr_start, curr_end))
            curr_start, curr_end = next_start, next_end

    merged_ranges.append((curr_start, curr_end))

total_count = 0
for start, end in merged_ranges:
    total_count += (end - start + 1)

print(total_count)