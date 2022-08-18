# 1219 1220 1259

import sys

sys.stdin = open("input.txt")

for test_count in range(1, 11):
    string_length, the_string = input().split()
    the_stack = [""]
    for i in the_string:
        # 이번 문자가 스택에 저장된 마지막 문자와 같다면 스택에서 삭제
        if i == the_stack[-1]:
            the_stack.pop()
        # 다르다면 스택에 추가
        else:
            the_stack.append(i)
    # 스택에 저장된 문자들을 붙혀서 출력
    print(f"#{test_count} ", *the_stack, sep="")
