# 조교의 성적 매기기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PwGK6AcIDFAUq

import sys

sys.stdin = open("input.txt")

for test_case in range(1, int(input()) + 1):
    student_amount, what_grade = map(int, input().split())
    all_scores = []
    for _ in range(student_amount):
        i, j, k = map(int, input().split())
        all_scores.append(i * (7 / 20) + j * (9 / 20) + k * (4 / 20))
    print(all_scores)
