def bfs(start_node):
    queue = []
    queue.append(start_node)
    while queue:
        next_node = queue.pop(0)
        if not visited[next_node]:
            visited[next_node] = True
            queue += graph_list[next_node]
            print(next_node, end=" ")


a = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

graph_list = [[] for _ in range(max(a) + 1)]
visited = [False for _ in range(max(a) + 1)]

for i in range(len(a)):
    if i & 1:
        graph_list[a[i - 1]].append(a[i])
        graph_list[a[i]].append(a[i - 1])
bfs(1)
