# 0958 1029


import sys

sys.stdin = open("input.txt")


for test_count in range(1, 11):
    test_count_not_use = input()
    N_list = []
    for _ in range(100):
        N_list.append(input())

    max_palindrome_count = 0
    # 각 행과 열을 결정할 숫자 범위
    for t in range(100):
        # 회문의 길이를 결정할 숫자 범위
        for i in range(1, 101):
            # 회문의 시작점을 결정할 숫자 범위
            for j in range(100 - i + 1):
                # 문자열 슬라이싱으로 잘라낸 후 회문인지 비교하고, 길이가 가장 길다면 최대값 갱신
                the_letters = N_list[t][j : j + i]
                if the_letters == the_letters[::-1] and max_palindrome_count < len(
                    the_letters
                ):
                    max_palindrome_count = len(the_letters)
                # 방금 비교를 위해 생성한 문자열을 초기화
                the_letters = ""
                # 열에서 회문의 길이만큼 문자를 하나씩 가져와 전부 더해 문자열을 생성
                for k in range(i):
                    the_letters += N_list[j + k][t]
                # 회문인지 확인하고 회문이면서 최대값이면 최대값 갱신
                if the_letters == the_letters[::-1] and max_palindrome_count < len(
                    the_letters
                ):
                    max_palindrome_count = len(the_letters)

    print(f"#{test_count}", max_palindrome_count)
