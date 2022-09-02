# 0921 0951

import sys

sys.stdin = open("input.txt")

T = int(input())

for test_count in range(1, T + 1):
    N, M = map(int, input().split())
    N_list = []
    for _ in range(N):
        N_list.append(input())
    # 가로에서 길이 M만큼 문자열 슬라이싱을 해나가며 회문인지 검토
    for i in N_list:
        for j in range(N - M + 1):
            the_letters = i[j : M + j]
            if the_letters == the_letters[::-1]:
                print(f"#{test_count}", the_letters)
    # 세로에서 길이 M만큼 반복하며 문자들을 더해나가며 문자열로 만들고 이것이 회문인지 검토
    for t in range(N):
        for k in range(N - M + 1):
            the_letters = ""
            for h in range(M):
                the_letters += N_list[k + h][t]
            if the_letters == the_letters[::-1]:
                print(f"#{test_count}", the_letters)
