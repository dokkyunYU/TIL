# 재미있는 오셀로 게임
# https: // swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId = AWQmA4uK8ygDFAXj
# 0948 1118

import sys
sys.stdin = open("sample_input.txt")


def game_play(row, col, depth):
    if not (0 <= row < board_length and 0 <= col < board_length) or game_board_list[row][col] == 0:
        return 0
    if depth != 0 and game_board_list[row][col] == color_now:
        return 1
    if game_play(row + direction[0], col + direction[1], depth + 1):
        game_board_list[row][col] = color_now
        return 1


delta_move = [0, -1, 1]
for test_count in range(1, int(input()) + 1):
    board_length, game_count = map(int, input().split())
    # 1: B , 2: W
    game_progress = [tuple(map(int, input().split())) for _ in range(game_count)]
    game_board_list = [[0] * board_length for _ in range(board_length)]
    game_board_list[board_length//2 - 1][board_length//2 - 1] = 2
    game_board_list[board_length // 2][board_length // 2] = 2
    game_board_list[board_length // 2][board_length // 2 - 1] = 1
    game_board_list[board_length // 2 - 1][board_length // 2] = 1
    while game_progress:
        row_now, col_now, color_now = game_progress.pop(0)
        game_board_list[row_now - 1][col_now - 1] = color_now
        for i in delta_move:
            for j in delta_move:
                if i == j == 0:
                    continue
                direction = (i, j)
                game_play(row_now - 1, col_now - 1, 0)
    black_count = 0
    white_count = 0
    for k in range(board_length):
        for t in range(board_length):
            if game_board_list[k][t] == 1:
                black_count += 1
            elif game_board_list[k][t] == 2:
                white_count += 1
    print("#{} {} {}".format(test_count, black_count, white_count))
