def dfs(start_node):
    visited[start_node] = True
    print(start_node, end=" ")
    for i in graph_list[start_node]:
        if not visited[i]:
            dfs(i)


a = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

graph_list = [[] for _ in range(max(a) + 1)]
visited = [False for _ in range(max(a) + 1)]

for i in range(len(a)):
    if i & 1:
        graph_list[a[i - 1]].append(a[i])
        graph_list[a[i]].append(a[i - 1])
dfs(1)
