import sys

sys.stdin = open("input.txt")

T = int(input())

for test_count in range(1, T + 1):
    N = int(input())
    N_list = []
    for _ in range(N):
        N_list.append(list(map(int, input().split())))
    absolute_sum = 0
    for ix in range(N):
        for iy in range(N):
            # 델타 검색은 결국 덧셈을 해서 변수를 하나 더 생성하고, 이후 if문 조건 검토 횟수도 별차이 없길래
            # 아래와 같이 넣어봤습니다.
            if ix > 0:
                absolute_sum += abs(N_list[ix][iy] - N_list[ix - 1][iy])
            if ix < N - 1:
                absolute_sum += abs(N_list[ix][iy] - N_list[ix + 1][iy])
            if iy > 0:
                absolute_sum += abs(N_list[ix][iy] - N_list[ix][iy - 1])
            if iy < N - 1:
                absolute_sum += abs(N_list[ix][iy] - N_list[ix][iy + 1])

    print(f"#{test_count} {absolute_sum}")
