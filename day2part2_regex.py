import re

pattern = re.compile(r"^(\d+)\1+$")

input = "day2.txt"
invalid_list = []

with open(input) as f:
    ranges = [tuple(map(int, x.split('-'))) for x in f.read().strip().split(',')]

for start, end in ranges:
    for number in range(start, end + 1):
        if pattern.match(str(number)):
            invalid_list.append(number)

print(sum(invalid_list))