input = "day3.txt"

battery_list = []

with open(input) as f:
    banks = [x.strip() for x in f.readlines()]

for i in banks:
    batteries = [int(x) for x in i]
    digit_1_ind = batteries.index(max(batteries[:-1]))
    batteries_rest = batteries[digit_1_ind+1:]
    digit_2_ind = digit_1_ind + batteries_rest.index(max(batteries_rest)) + 1
    battery_list.append(batteries[digit_1_ind]*10 + batteries[digit_2_ind])

print(sum(battery_list))

