n = int(input())

column_list = [list(map(int, input().split())) for _ in range(n)]

column_list = sorted(column_list, key=lambda x: x[0])

result = 0
max_value = max(column_list, key=lambda x: x[1])
max_idx = []
for i in column_list:
    if i[1] == max_value[1]:
        max_idx.append(i[0])


result += (max_idx[-1] - max_idx[0] + 1) * max_value[1]

prev_height = 0
prev_idx = 0
for j in column_list:
    # print(j[0], max_idx, max_value)
    if prev_height == 0:
        prev_idx = j[0]
        prev_height = j[1]
    else:
        if j[1] > prev_height:
            result += (j[0] - prev_idx) * prev_height
            prev_idx = j[0]
            prev_height = j[1]
            if j[0] == max_idx[0]:
                break


prev_height = 0
prev_idx = 0

for k in column_list[::-1]:
    if prev_height == 0:
        prev_idx = k[0]
        prev_height = k[1]
    else:
        if k[1] > prev_height:
            result += (prev_idx - k[0]) * prev_height
            prev_idx = k[0]
            prev_height = k[1]
            if k[0] == max_idx[-1]:
                break

print(result)