import numpy as np

input_file = "day6.txt"
answer = []

with open(input_file) as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

number_lines = lines[:-1]
symbol_line = lines[-1]

matrix = np.array([list(map(int, line.split())) for line in number_lines])
symbols = symbol_line.split()

for i in range(matrix.shape[1]):
    if symbols[i] == "+":
        answer.append(np.sum(matrix[:,i]))
    elif symbols[i] == "*":
        answer.append(np.prod(matrix[:,i]))

print (sum(answer))


