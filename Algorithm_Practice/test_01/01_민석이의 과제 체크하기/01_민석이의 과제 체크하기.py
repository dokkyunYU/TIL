# 01_민석이의 과제 체크하기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWVl3rWKDBYDFAXm&
# 0.25


import sys

sys.stdin = open("input.txt")

t = int(input())

for test_count in range(1, t + 1):
    n, k = map(int, input().split())
    students_homework = list(range(1, n + 1))
    homework_done = list(map(int, input().split()))
    homework_not_done = []
    for i in students_homework:
        if i not in homework_done:
            homework_not_done.append(i)
    print(f"#{test_count}", *homework_not_done)
