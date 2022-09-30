from heapq import heappop, heappush
import sys

sys.stdin = open("input.txt")

house_cnt, road_cnt = map(int, input().split())
heap = []
heap2 = []
visited = [False]*(house_cnt + 1)
distance = [[] for _ in range(house_cnt + 1)]

for _ in range(road_cnt):
    h1, h2, road_cost = map(int, sys.stdin.readline().split())
    heappush(heap2, (road_cost, h1))
    distance[h1].append((road_cost, h2))
    distance[h2].append((road_cost, h1))
total_cost = 0
count_up = 0
max_cost = 0
starting = heappop(heap2)[1]
for i in distance[starting]:
    heappush(heap, i)
visited[starting] = True
while heap:
    road_cost, h3 = heappop(heap)
    if not(visited[h3]):
        visited[h3] = True
        total_cost += road_cost
        if road_cost > max_cost:
            max_cost = road_cost
        for i in distance[h3]:
            if not visited[i[1]]:
                heappush(heap, i)
        count_up += 1
        if count_up == house_cnt - 1:
            break
print(total_cost - max_cost)
