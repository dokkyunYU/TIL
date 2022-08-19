# 06_등산로 조성
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq
# 1626

import sys

sys.stdin = open("input.txt")

def sliding_down():
    road_length = 0
    for digging in range(dig_depth):
        if digging

    return road_length



t = int(input())

for test_count in range(1, t+1):
    square, dig_depth = map(int, input().split())
    square_list = [list(map(int, input().split())) for _ in range(square)]
    # 땅 파기 전의 최소값
    # 최대값과 그 위치들을 구해야한다