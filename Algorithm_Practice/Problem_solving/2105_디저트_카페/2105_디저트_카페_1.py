# 디저트 카페
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu
# 1331 1543

import sys
sys.stdin = open("sample_input.txt")

def diagonal_move(row, col, move_dir=0, move_count=0, depth=1):
    if not(0 <= row < area_size and 0 <= col < area_size):
        return
    dessert_set.add(area_dessert_list[row][col])
    if len(dessert_set) < depth:
        return
    if row - 1 == row_now and col + 1 == col_now:
        answer_set.add(len(dessert_set))
        # print(depth)
        dessert_set.discard(area_dessert_list[row][col])
        return
    if move_dir < 1:
        diagonal_move(row + 1, col + 1, 0, move_count + 1, depth + 1)
    if depth > 1 and move_dir < 2:
        diagonal_move(row + 1, col - 1, 1, move_count, depth + 1)
    if depth > 1 and move_count > 0 and move_dir < 3:
        diagonal_move(row - 1, col - 1, 2, move_count - 1, depth + 1)
    if depth > 1 and move_dir < 4:
        diagonal_move(row - 1, col + 1, 3, move_count, depth + 1)
    dessert_set.discard(area_dessert_list[row][col])


for test_count in range(1, int(input()) + 1):
    area_size = int(input())
    area_dessert_list = [list(map(int, input().split())) for _ in range(area_size)]
    dessert_set = set()
    answer_set = set()
    for row_now in range(area_size):
        for col_now in range(area_size):
            # print("start")
            diagonal_move(row_now, col_now)
    print("#{} {}".format(test_count, max(answer_set) if answer_set else -1))
