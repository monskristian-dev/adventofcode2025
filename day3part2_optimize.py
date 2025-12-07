input = "day3.txt"
battery_list = []

with open(input) as f:
    for line in f:
        batteries = [int(x) for x in line.strip()]
        total_digits = 12
        index_current = 0
        value_current = 0
        for i in range(total_digits):
            remaining_digits = total_digits - 1 - i
            end_slice = -remaining_digits if remaining_digits > 0 else None
            window = batteries[index_current:end_slice]
            digit = max(window)
            digit_ind = window.index(digit)
            value_current = (value_current*10) + digit
            index_current += digit_ind + 1
        
        battery_list.append(value_current)

#print(battery_list)
print(sum(battery_list))

