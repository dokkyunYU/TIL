# 03_통역사 성경이
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWqPvqoqSLQDFAT_
# 1424 1444

import sys

sys.stdin = open("input.txt")

t = int(input())

for test_count in range(1,t+1):
    n = int(input())
    input_string: str = input().split()
    name_count = [0]*n
    idx = 0
    is_end = False
    text = ""
    for j in input_string:
        if j[-1] in [".", "?", "!"]:
            text = j[:len(j)-1]
            is_end = True
        else :
            text = j
        if text[0].isupper():
            for k in range(1, len(text)):
                if not text[k].islower():
                    break
            else:
                name_count[idx] += 1
        if is_end:
            idx += 1
            is_end = False
    print(f"#{test_count}", *name_count)