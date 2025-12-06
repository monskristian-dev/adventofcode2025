input = "day1.txt"

direction = {"L": -1, "R": 1}
init = 50
codes = []

for i in open(input):
    for j in range(int(float(i[1:]))):
        newnum = init + direction[i[0]]
        if newnum > 99:
            newnum = 0
        elif newnum < 0:
            newnum = 99
        else:
            pass
        codes.append(newnum)
        init = newnum

print(codes.count(0.0))