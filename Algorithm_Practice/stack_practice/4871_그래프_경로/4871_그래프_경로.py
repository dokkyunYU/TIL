# 1442

import sys

sys.stdin = open("input.txt")


def find_route(start, end):
    route_list = []
    is_this_node_correct = [True] * (nodes_numbers + 1)
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


T = int(input())

for test_count in range(1, T + 1):
    nodes_numbers, line_numbers = map(int, input().split())
    node_list = [[] for _ in range(nodes_numbers + 1)]
    for _ in range(line_numbers):
        idx1, idx2 = map(int, input().split())
        node_list[idx1].append(idx2)

    start, end = map(int, input().split())

    print(f"#{test_count}", find_route(start, end))
