import numpy as np

input_file = "day7.txt"

with open(input_file) as f:
    lines = [line.strip() for line in f.readlines()]

answer = np.zeros(len(lines[0]))

initial = lines[0].index("S")
answer[initial] = 1

for i in range(len(lines)-1):
    for j in range(len(lines[i])):
        if lines[i+1][j] == "^":
            answer[j-1] += answer[j]
            answer[j+1] += answer[j]
            answer[j] = 0

print (answer.sum())


