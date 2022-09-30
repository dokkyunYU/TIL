# 하나로
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15StKqAQkCFAYD&
# 1047 1129

import sys
from heapq import heappop, heappush

sys.stdin = open("input.txt")


def dist_func(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


for test_count in range(1, int(input()) + 1):
    islands_cnt = int(input())
    islands = [i for i in zip(map(int, input().split()), map(int, input().split()))]
    eco_cost = float(input())
    distance_list = []
    visited = [False] * islands_cnt
    heap = []
    for i in range(islands_cnt):
        dist_list = []
        for j in range(islands_cnt):
            if i != j:
                dist_list.append((dist_func(islands[i], islands[j]), j))
        distance_list.append(dist_list)
    for i in distance_list[0]:
        heappush(heap, i)
    visited[0] = True
    total_cost = 0
    count_up = 0
    while heap:
        dist, next_i = heappop(heap)
        if not visited[next_i]:
            visited[next_i] = True
            total_cost += dist
            count_up += 1
            if count_up == islands_cnt - 1:
                break
            for i in distance_list[next_i]:
                heappush(heap, i)
    print(f"#{test_count}", round(total_cost * eco_cost))
