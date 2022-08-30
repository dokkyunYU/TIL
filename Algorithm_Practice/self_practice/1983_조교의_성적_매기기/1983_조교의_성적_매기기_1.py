# 조교의 성적 매기기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PwGK6AcIDFAUq

import sys

# from filecmp import cmp

sys.stdin = open("input.txt")
# sys.stdout = open("output2.txt", "w")

for test_case in range(1, int(input()) + 1):
    student_amount, what_grade = map(int, input().split())
    all_scores = []
    for _ in range(student_amount):
        i, j, k = map(int, input().split())
        all_scores.append(i * (7 / 20) + j * (9 / 20) + k * (4 / 20))
    want_to_know = all_scores[what_grade - 1]
    all_scores.sort()
    the_grade = all_scores.index(want_to_know) // (student_amount // 10)
    grade_list = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']
    print(f"#{test_case}", grade_list[the_grade])

# print(cmp('output.txt', 'output2.txt'))
