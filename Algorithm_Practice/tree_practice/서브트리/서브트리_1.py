# subtree
# 1016 1235

import sys
sys.stdin = open("sample_input.txt")

for test_count in range(1, int(input()) + 1):
    lines_count, starting_root = map(int, input().split())
    lines_list = list(map(int, input().split()))
    tree_list = [[] for _ in range(lines_count + 2)]
    for i in range(len(lines_list)):
        if i & 1:
            tree_list[lines_list[i - 1]].append(lines_list[i])
    # BFS의 개념을 활용한다
    # 방문해야할 노드를 큐에 저장해두고 큐에서 pop된 노드에 방문할 때마다 카운트를 하나씩 상승
    search_queue = [starting_root]
    sub_tree_count = 0
    # 더이상 큐 리스트가 없을때까지 반복한다
    while search_queue:
        # 자식노드들을 저장해둔 리스트를 불러와 큐 리스트에 더한다
        search_queue += tree_list[search_queue.pop(0)]
        sub_tree_count += 1
    print(f"#{test_count}", sub_tree_count)
