import sys

sys.stdin = open("input.txt")


def ladder_travel(given_list):
    idx_row = len(given_list) - 1
    # 도착점 찾기
    idx_col = 0
    for i, j in enumerate(given_list[idx_row]):
        if j == 2:
            idx_col = i

    while idx_row != 0:
        # 움직일 방향 설정
        direction = 0
        # idx_col이 0보다 크다면 왼쪽을 검토해서 1인지 확인
        if idx_col > 0 and given_list[idx_row][idx_col - 1] == 1:
            direction = -1
        # idx_col이 99보다 작다면 오른쪽을 검토해서 1인지 확인
        if idx_col < 99 and given_list[idx_row][idx_col + 1] == 1:
            direction = 1
        # direction이 0이 아닐때, 1이라고 확인된 쪽을 향해 0~99이면서 1이 나오는 동안 계속 전진
        while (
            0 <= idx_col + direction <= 99
            and given_list[idx_row][idx_col + direction]
            and direction
        ):
            idx_col += direction
            # print("-", idx_row, idx_col, given_list[idx_row][idx_col])
        idx_row -= 1
        # print("|", idx_row, idx_col, given_list[idx_row][idx_col])
    return idx_col


for test_count in range(1, 11):
    ladder_list = []
    T = int(input())
    for _ in range(100):
        ladder_list.append(list(map(int, input().split())))

    print(f"#{T}", ladder_travel(ladder_list))


# 1.40
