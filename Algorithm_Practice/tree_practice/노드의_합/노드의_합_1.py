# 노드의 합
# 1238 1349

import sys
sys.stdin = open("sample_input.txt")


def sumorder(node_num):
    # 만약 받은 노드 넘버가 트리 리스트 범위 내에 있으면
    if node_num <= node_count:
        # 현재 위치한 노드의 값과 자식 노드들 합을 더해서 반환한다
        # 이렇게 해야 말단의 노드가 자신의 값을 반환한다 말단 노드 이상에서는 별 의미 없다
        return complete_binary_tree[node_num] + sumorder(2 * node_num) + sumorder(2 * node_num + 1)
    # 호출되었을때 그 노드 넘버가 범위를 초과했다면, 즉 호출한 노드가 자식노드를 가지고 있지 않다면
    else:
        # 0을 반환한다
        return 0


for test_count in range(1, int(input()) + 1):
    node_count, leaf_node, print_node = map(int, input().split())
    complete_binary_tree = [0 for _ in range(node_count + 1)]
    # 말단 노드들에 값을 입력하고 이외의 노드값은 전부 0으로 남겨둔다
    for _ in range(leaf_node):
        idx, input_number = map(int, input().split())
        complete_binary_tree[idx] = input_number
    print(f"#{test_count}", sumorder(print_node))
