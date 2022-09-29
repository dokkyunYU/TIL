from heapq import heappop, heappush

node_count = int(input())
line_count = int(input())
heap = []
total_cost = 0
loof_count = 0
visited = [False] * (node_count + 1)
for _ in range(line_count):
    heappush(heap, tuple(list(map(int, input().split()))[::-1]))
while heap:
    length, n, m = heappop(heap)
    if not(visited[n] and visited[m]):
        visited[n] = visited[m] = True
    total_cost += length
    loof_count
    if loof_count == node_count - 1:
        break
print(total_cost)
