input = "day1.txt"

direction = {"L": -1, "R": 1}
init = 50
codes = []

for i in open(input):
    newnum = init + direction[i[0]] * float(i[1:])
    codes.append(newnum % 100)
    init = newnum % 100

print(codes.count(0.0))