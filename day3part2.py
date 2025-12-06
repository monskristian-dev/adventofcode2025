input = "day3.txt"
battery_list = []
digits = []

with open(input) as f:
    banks = [x.strip() for x in f.readlines()]

for i in banks:
    batteries = [int(x) for x in i]
    digit_1_ind = batteries.index(max(batteries[:-11]))
    batteries_rest = batteries[digit_1_ind+1:-10]
    digit_2_ind = digit_1_ind + batteries_rest.index(max(batteries_rest)) + 1
    batteries_rest = batteries[digit_2_ind+1:-9]
    digit_3_ind = digit_2_ind + batteries_rest.index(max(batteries_rest)) + 1
    batteries_rest = batteries[digit_3_ind+1:-8]
    digit_4_ind = digit_3_ind + batteries_rest.index(max(batteries_rest)) + 1
    batteries_rest = batteries[digit_4_ind+1:-7]
    digit_5_ind = digit_4_ind + batteries_rest.index(max(batteries_rest)) + 1
    batteries_rest = batteries[digit_5_ind+1:-6]
    digit_6_ind = digit_5_ind + batteries_rest.index(max(batteries_rest)) + 1
    batteries_rest = batteries[digit_6_ind+1:-5]
    digit_7_ind = digit_6_ind + batteries_rest.index(max(batteries_rest)) + 1
    batteries_rest = batteries[digit_7_ind+1:-4]
    digit_8_ind = digit_7_ind + batteries_rest.index(max(batteries_rest)) + 1
    batteries_rest = batteries[digit_8_ind+1:-3]
    digit_9_ind = digit_8_ind + batteries_rest.index(max(batteries_rest)) + 1
    batteries_rest = batteries[digit_9_ind+1:-2]
    digit_10_ind = digit_9_ind + batteries_rest.index(max(batteries_rest)) + 1
    batteries_rest = batteries[digit_10_ind+1:-1]
    digit_11_ind = digit_10_ind + batteries_rest.index(max(batteries_rest)) + 1
    batteries_rest = batteries[digit_11_ind+1:]
    digit_12_ind = digit_11_ind + batteries_rest.index(max(batteries_rest)) + 1
    battery_list.append(batteries[digit_1_ind]*100000000000 + batteries[digit_2_ind]*10000000000 + batteries[digit_3_ind]*1000000000 + batteries[digit_4_ind]*100000000 + batteries[digit_5_ind]*10000000 + batteries[digit_6_ind]*1000000+ batteries[digit_7_ind]*100000+ batteries[digit_8_ind]*10000 + batteries[digit_9_ind]*1000 + batteries[digit_10_ind]*100 + batteries[digit_11_ind]*10 + batteries[digit_12_ind])

print(sum(battery_list))

