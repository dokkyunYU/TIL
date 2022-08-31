# 1156 1220 1256 1303
import sys

sys.stdin = open("input.txt")

alien_numbers_list = [
    [0, "ZRO"],
    [1, "ONE"],
    [2, "TWO"],
    [3, "THR"],
    [4, "FOR"],
    [5, "FIV"],
    [6, "SIX"],
    [7, "SVN"],
    [8, "EGT"],
    [9, "NIN"],
]

T = int(input())

for test_count in range(1, 11):
    test_number, N = input().split()
    given_numbers_list = [0] * 10
    for i in input().split():
        for j in alien_numbers_list:
            # 외계인 숫자를 인류 숫자에 대응시켜 카운팅 정렬
            if j[1] == i:
                given_numbers_list[j[0]] += 1
    print(f"{test_number}")
    for k in range(10):
        # 인류 숫자가 나온 숫자만큼 외계인 숫자를 반복 출력
        print(*([alien_numbers_list[k][1]] * given_numbers_list[k]))

# 0.40
