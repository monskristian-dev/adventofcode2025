import math

input_file = "day6.txt"
answer = []
digitss = []
digitsss = []
symbolcounter = 0

with open(input_file) as f:
    lines = [line for line in f.readlines()]

number_lines = lines[:-1]
symbols = lines[-1].strip().split()[::-1]

symbols = [x[::-1] for x in symbols]
number_lines = [x.replace("\n","0").replace(" ","0") for x in number_lines]

digits = [x[::-1] for x in number_lines]

for i in range(len(digits[0])):
    bool_list_num = [x[i] for x in digits]
    bool_list = [x == "0" for x in bool_list_num]
    if all(bool_list) == True:
        digitsss.append(digitss)
        digitss = []
    else:
        digits_topdown = ("").join([x[i] for x in digits]).strip("0")
        digitss.append(int(digits_topdown))

digitsss.append(digitss)
digitsss.pop(0)

for i in range(len(digitsss)):
    if symbols[symbolcounter] == "+":
        answer.append(sum(digitsss[i]))
    elif symbols[symbolcounter] == "*":
        answer.append(math.prod(digitsss[i]))
    symbolcounter += 1

print (sum(answer))