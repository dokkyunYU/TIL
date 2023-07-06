cnt_dict = {}
max_val = 0
max_key = ""
for i in input():
    i = i.upper()
    if i in cnt_dict:
        cnt_dict[i] += 1
    else:
        cnt_dict[i] = 1
for i, j in cnt_dict.items():
    if j == max_val:
        max_key = "?"
        break
    elif j > max_val:
        max_val = j
        max_key = i
print(max_key)
