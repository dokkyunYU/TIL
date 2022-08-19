# 05_창용마을 무리의 개수
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWngfZVa9XwDFAQU
# 1551 1621

import sys

sys.stdin = open("input.txt")

def well_known(start: int):
    if already_known[start]:
        return 0
    else:
        already_known[start] = True
        now_location = start
        route_stack = []
        while True:
            for i in people_list[now_location]:
                if not already_known[i]:
                    route_stack.append(now_location)
                    now_location = i
                    already_known[now_location] = True
                    break
            else:
                if not route_stack:
                    return 1
                now_location = route_stack.pop()


t = int(input())

for test_count in range(1, t+1):
    people_number, line_number = map(int, input().split())
    people_list = [[] for _ in range(people_number + 1)]
    already_known = [False for _ in range(people_number + 1)]
    result = 0
    for _ in range(line_number):
        person1, person2 = map(int, input().split())
        people_list[person1].append(person2)
        people_list[person2].append(person1)
    for i in range(1, people_number + 1):
        result += well_known(i)
    print(f"#{test_count}", result)