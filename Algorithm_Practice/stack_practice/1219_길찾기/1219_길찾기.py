# 1219 길찾기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14geLqABQCFAYD

# 1600 1725

import sys

sys.stdin = open("input.txt")


def find_route(start, end):
    route_list = []
    is_this_node_correct = [True] * (100)
    now_location = start
    while True:
        for i in range(len(node_list[now_location])):
            if is_this_node_correct[node_list[now_location][i]]:
                route_list.append(now_location)
                is_this_node_correct[now_location] = False
                now_location = node_list[now_location][i]
                if now_location == end:
                    return 1
                break
        else:
            is_this_node_correct[now_location] = False
            if len(route_list) == 0:
                return 0
            now_location = route_list.pop()


# T = int(input())

for test_count in range(1, 11):
    test_counts, couple_numbers = map(int, input().split())
    couple_list = list(map(int, input().split()))
    node_list = [[] for _ in range(100)]
    for i in range(couple_numbers):
        node_list[couple_list[2 * i]].append(couple_list[2 * i + 1])
    start, end = 0, 99

    print(f"#{test_count}", find_route(start, end))
