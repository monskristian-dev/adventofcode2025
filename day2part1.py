input = "day2.txt"

invalid_list = []

range_ID_list = [i.split(",") for i in open(input)]
range_ID = [i.split("-") for i in range_ID_list[0]]

for i in range(len(range_ID)):
    for j in range(int(range_ID[i][1])-int(range_ID[i][0])+1):
        number = int(range_ID[i][0]) + j
        number_str = str(number)
        window = len(number_str) / 2
        if (window == int(window)):
            guess = int(number_str[:int(window)])
            if (int(number_str[int(window):]) == guess):
                invalid_list.append(number)
        else:
            pass

print(sum(invalid_list))