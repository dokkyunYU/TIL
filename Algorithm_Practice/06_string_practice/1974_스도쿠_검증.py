# 0.40

import sys

sys.stdin = open("input.txt")

T = int(input())

for test_count in range(1, T + 1):
    sudoku_list = []
    for _ in range(9):
        sudoku_list.append(list(map(int, input().split())))
    is_this_ok = True
    for i in range(9):
        sudoku_set1 = set()
        sudoku_set2 = set()
        for j in range(9):
            sudoku_set1.add(sudoku_list[i][j])
            sudoku_set2.add(sudoku_list[j][i])
        if len(sudoku_set1) != 9 or len(sudoku_set2) != 9:
            is_this_ok = False
            break
    want_break = False
    for t in range(3):
        if not want_break:
            for k in range(3):
                sudoku_set1 = set()
                for i in range(3 * t, 3 * t + 3):
                    for j in range(3 * k, 3 * k + 3):
                        sudoku_set1.add(sudoku_list[i][j])
                if len(sudoku_set1) != 9:
                    is_this_ok = False
                    want_break = True
                    break
        else:
            break

    print(f"#{test_count}", int(is_this_ok))
