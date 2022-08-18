# 1152 1215

import sys

sys.stdin = open("input.txt")

T = int(input())

for test_count in range(1, T + 1):
    the_string = input()
    prev_letter = ""
    remove_idx = []
    while True:
        for i in range(len(the_string)):
            # 이번 문자가 이전 문자와 같다면 문자열에서 삭제하고 for문 탈출
            if the_string[i] == prev_letter:
                the_string = the_string[: i - 1] + the_string[i + 1 :]
                prev_letter = ""
                break
            # 다르다면 이전문자를 지금문자로 갱신
            else:
                prev_letter = the_string[i]
        # 같은 문자를 한번도 찾지 못했다면 while문 탈출
        else:
            break
    print(f"#{test_count}", len(the_string))
