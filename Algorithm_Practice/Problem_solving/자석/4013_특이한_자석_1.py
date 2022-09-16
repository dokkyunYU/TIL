# 특이한 자석
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeV9sKkcoDFAVH&&
# 1938 2116

import sys


def magnet_rotation(magnet_number, rotate_direction):
    global is_linked
    # 일단 돌아가는 방향을 정한다
    is_linked[magnet_number] = rotate_direction
    # magnet_number가 1보다 크고, 연결 판정이 0일 경우
    if magnet_number > 1 and is_linked[magnet_number - 1] == 0:
        # 그리고 맞닿는 부분의 극성이 다를 경우
        if magnets[magnet_number - 1][2] != magnets[magnet_number][6]:
            # magnet_number - 1과 회전 방향에 마이너스를 붙힌 숫자를 써서 현재 함수를 재호출한다
            magnet_rotation(magnet_number - 1, -rotate_direction)
    # magnet_number가 4보다 작고, 연결 판정이 0일 경우
    if magnet_number < 4 and is_linked[magnet_number + 1] == 0:
        # 그리고 맞닿는 부분의 극성이 다를 경우
        if magnets[magnet_number + 1][6] != magnets[magnet_number][2]:
            # magnet_number + 1과 회전 방향에 마이너스를 붙힌 숫자를 써서 현재 함수를 재호출한다
            magnet_rotation(magnet_number + 1, -rotate_direction)


sys.stdin = open("sample_input.txt")

for test_count in range(1, int(input()) + 1):
    rotate_count = int(input())
    magnets = [0]
    # 각 자석의 번호에 자석의 리스트를 넣어준다
    for _ in range(4):
        magnets.append(list(map(int, input().split())))
    for _ in range(rotate_count):
        # 연결이 되었는지 아닌지를 판정하는 리스트를 초기화
        is_linked = [0] * 5
        magnet_num, rotate_dir = map(int, input().split())
        magnet_rotation(magnet_num, rotate_dir)
        # 1 ~ 4까지, 연결 판정에 따라 자석을 회전
        for i in range(1, 5):
            if is_linked[i] == 1:
                magnets[i].insert(0, magnets[i].pop())
            if is_linked[i] == -1:
                magnets[i].append(magnets[i].pop(0))
    result_sum = 0
    for j in range(1, 5):
        # 2의 (각 자석 번호 - 1) 승수만큼 커지므로
        result_sum += magnets[j][0] * (2 ** (j - 1))
    print(f"#{test_count}", result_sum)
