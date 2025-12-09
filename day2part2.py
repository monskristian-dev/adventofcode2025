import math
import textwrap

input = "day2.txt"

invalid_list = []
bool_list = []

range_ID_list = [i.split(",") for i in open(input)]
range_ID = [i.split("-") for i in range_ID_list[0]]

for i in range(len(range_ID)):
    for j in range(int(range_ID[i][1])-int(range_ID[i][0])+1):
        number = int(range_ID[i][0]) + j
        number_str = str(number)
        window_max = math.ceil(len(number_str) / 2)
        if (len(number_str) == 1):
            pass
        else:
            for k in range(1,window_max+1):
                guess = number_str[:k]
                window_ins = (len(number_str) / k)
                if window_ins == int(window_ins):
                    chunks = textwrap.wrap(number_str,k)
                    if len(set(chunks)) == 1:
                        invalid_list.append(number)
                        break
                    else:
                        pass
                else:
                    pass

print(sum(invalid_list))