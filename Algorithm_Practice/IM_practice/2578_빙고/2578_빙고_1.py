# 1424 1713

import sys

sys.stdin = open("input.txt")
# 숫자 리스트
number_list = [list(map(int, input().split())) for _ in range(5)]
# 사회자가 부르는 숫자 리스트
call_list = []
for _ in range(5):
    call_list += list(map(int, input().split()))
# 각 숫자의 좌표값을 저장하는 리스트
coordinate_list = [0]*26
# 각 좌표값이 몇개 나왔는지 세는 리스트
x_idx_count = [0] * 5
y_idx_count = [0] * 5
# 대각선상에 존재하는 숫자들을 저장하는 세트
diagonal_set1 = set()
diagonal_set2 = set()
# 좌표값과 대각선 숫자들을 저장하는 이중for문
for i in range(5):
    for j in range(5):
        coordinate_list[number_list[i][j]] = (i, j)
        if i == j:
            diagonal_set1.add(number_list[i][j])
        if i + j == 4:
            diagonal_set2.add(number_list[i][j])
bingo_count = 0
for num, k in enumerate(call_list, start=1):
    # print(k)
    # print(diagonal_set1, diagonal_set2)
    # print(coordinate_list)
    # print(x_idx_count)
    # print(y_idx_count)
    # 사회자가 부르는 숫자가 있으면 세트를 제거
    diagonal_set1.discard(k)
    diagonal_set2.discard(k)
    # 사회자가 부르는 숫자의 좌표값에 해당하는 숫자에 횟수 추가
    x_idx_count[coordinate_list[k][0]] += 1
    y_idx_count[coordinate_list[k][1]] += 1
    # 하나의 행 혹은 열이 5번 나왔다면 빙고
    if x_idx_count[coordinate_list[k][0]] == 5:
        bingo_count += 1
    if y_idx_count[coordinate_list[k][1]] == 5:
        bingo_count += 1
    # 대각선 세트가 완전히 비었다면 빙고
    # 여러번 빙고를 부르는것을 막기 위해 제거될 일 없는 숫자를 추가
    if not diagonal_set1:
        diagonal_set1.add(-1)
        bingo_count += 1
    if not diagonal_set2:
        diagonal_set2.add(-1)
        bingo_count += 1
    # 빙고가 3개라면 현재 숫자 순서를 프린트하고 break
    if bingo_count >= 3:
        print(num)
        break
