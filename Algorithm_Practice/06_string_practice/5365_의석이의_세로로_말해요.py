# 1038 1108

import sys

sys.stdin = open("input.txt")

T = int(input())

for test_count in range(1, T + 1):
    the_list = []
    for _ in range(5):
        the_list.append(list(input()))
    # 최대길이 15중에서 남은 부분에 전부 공백문자를 추가
    for i in range(5):
        for _ in range(15 - len(the_list[i])):
            the_list[i] += [""]
    result_letters = ""
    # 모든 열을 순회하며 문자들을 더해 문자열을 생성
    for j in range(15):
        for k in range(5):
            result_letters += the_list[k][j]

    print(f"#{test_count}", result_letters)
