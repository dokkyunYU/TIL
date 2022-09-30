# 특정한 최단 경로
# 1550

import sys

sys.stdin = open("input.txt")

INF = float("inf")
node_cnt, line_cnt = map(int, input().split())
node_list = [[0]*(node_cnt+1) for _ in range(node_cnt+1)]
for _ in range(line_cnt):
    row, col, dist = map(int, input().split())
    node_list[row][col] = node_list[col][row] = dist
essential1, essential2 = map(int, input().split())
distance = [INF]*(node_cnt+1)
visited = [False]*(node_cnt+1)
starting = 1
visited[starting] = True
distance[starting] = 0
for i in range(starting + 1, node_cnt + 1):
    if node_list[starting][i] > 0:
        distance[i] = node_list[starting][i]
print(distance)
for _ in range(node_cnt - 1):
    min_dist = INF
    min_node = 0
    for i in range(1, node_cnt + 1):
        if not visited[i] and min_dist > distance[i]:
            min_dist = distance[i]
            min_node = i

    visited[min_node] = True

    for i in range(1, node_cnt):
        new_dist = distance[min_node] + node_list[min_node][i]
        if new_dist < distance[i]:
            distance[i] = new_dist

print(distance, visited)
print(*node_list, sep="\n")