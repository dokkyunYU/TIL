T = 10
# BFS 함수 정의


def bfs(v):
    visit = [0] * 101
    queue = [v]
    visit[v] = 1
    while queue:
        t = queue.pop(0)
        for j in adj_list[t]:
            if not visit[j]:
                queue.append(j)
                visit[j] = visit[t] + 1

    idx = []
    for k in range(101):
        if visit[k] == max(visit):
            idx.append(k)

    return max(idx)


for TC in range(1, T+1):
    Len, SN = map(int, input().split())
    arr = list(map(int, input().split()))

    adj_list = [[] for _ in range(101)]  # 노드 마다 이어진 노드를 표시
    for i in range(0, Len, 2):  # 범위 반복
        if arr[i+1] not in adj_list[arr[i]]:
            adj_list[arr[i]].append(arr[i+1])

    print(f'#{TC} {bfs(SN)}')
