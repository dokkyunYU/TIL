# 격자판의 숫자 이어 붙이기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7I5fgqEogDFAXB
# 1122 1139

import sys
sys.stdin = open("sample_input.txt")

def board_move(start_x, start_y, number_now):
    if not (0 <= start_x < 4 and 0 <= start_y < 4):
        return
    number_now += board_list[start_x][start_y]
    if len(number_now) == 7:
        numbers_set.add(number_now)
        return
    for k in range(4):
        board_move(start_x + dx[k], start_y + dy[k], number_now)


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for test_count in range(1, int(input()) + 1):
    board_list = [input().split() for _ in range(4)]
    numbers_set = set()
    number = ""
    for i in range(4):
        for j in range(4):
            board_move(i, j, number)
    print("#%d %d" %(test_count, len(numbers_set)))
