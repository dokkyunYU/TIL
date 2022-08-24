import sys

sys.stdin = open("input.txt")

T = int(input())

for test_count in range(1, T + 1):
    N, M = map(int, input().split())
    N_list = []
    for n in range(N):
        N_list.append(list(map(int, input().split())))
    # 전체 최대값 초기화
    max_flies_sum = 0
    # M x M 리스트를 움직이기 위한 좌표들의 2중 for문
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            # M x M 리스트 내부의 파리 총합 초기화
            flies_sum = 0
            # M x M 리스트 내의 총합을 구하여 최대값을 찾는 2중 for문
            for m in range(M):
                for k in range(M):
                    flies_sum += N_list[m + i][k + j]
                    if max_flies_sum < flies_sum:
                        max_flies_sum = flies_sum

    print(f"#{test_count}", max_flies_sum)

# 0.30
