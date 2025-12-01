code = "input.txt"
direction = {"L": -1, "R": 1}
init = 50
codes = []

for i in open(code):
    newnum = init + direction[i[0]] * float(i[1:-1])
    init = newnum
    code = newnum % 100
    codes += [code]

print (codes.count(0.0))