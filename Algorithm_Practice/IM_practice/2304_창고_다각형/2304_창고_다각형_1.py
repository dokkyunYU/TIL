# 창고다각형
# https://www.acmicpc.net/problem/2304
# 1500 1730
import sys

sys.stdin = open("input.txt")


# 변화율에 주목
# 현재의 높이를 current_height 과거의 높이를 prev_height
# current - prev < 0 일때 무시, > 0 일때 prev * (current_idx - prev_idx)
# < 0 일때 리스트 생성후


# 최대값들을 찾는다

# 최대값들 사이의 수들은 전부 무시

# 최대값이 하나라면, 최대값까지는 원래 알고리즘대로
# 이후 리스트에서 다시 최대값 검색
# 그 최대값까지 나아감
# 다시 최대값 검색
# 이후 반복

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
