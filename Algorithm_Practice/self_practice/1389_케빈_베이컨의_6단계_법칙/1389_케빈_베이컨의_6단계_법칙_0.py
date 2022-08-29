import sys
from collections import deque

N, M = map(int, input().split())
adj = {x + 1: [] for x in range(N)}
for i in range(M):
    s, e = map(int, sys.stdin.readline().split())

    adj[s].append(e)
    adj[e].append(s)

# print(adj)
b_num = float("inf")
b_people = 0

for i in range(1, N + 1):
    visited = [-1] * (N + 1)
    q = deque([i])
    visited[i] = 0
    while q:
        c = q.popleft()
        for neighbor in adj[c]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[c] + 1
                q.append(neighbor)

    if sum(visited) + 1 < b_num:
        b_num = sum(visited) + 1
        b_people = i
    # print(b_people, b_num)
print(b_people)
