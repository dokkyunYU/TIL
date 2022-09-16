# 이진탐색
# 1353 1423

import sys
sys.stdin = open("sample_input.txt")


def inorder_wright(node_num):
    # 노드에 쓸 숫자를 정의해둔다
    global wright_num
    # 노드 번호가 범위 내에 있을때만
    if node_num <= tree_length:
        # 왼쪽 자식 노드를 탐색한다
        inorder_wright(2 * node_num)
        # 탐색하고 돌아오거나 아니면 자식 노드가 없어서 그냥 돌아오면
        # 이후 지금 노드에 숫자를 쓴다
        complete_b_tree[node_num] = wright_num
        # 숫자를 한번이라도 썼다면 바로 1 증가시킨다
        wright_num += 1
        # 이후 오른쪽 자식 노드를 탐색한다
        inorder_wright(2 * node_num + 1)


for test_count in range(1, int(input()) + 1):
    tree_length = int(input())
    wright_num = 1
    complete_b_tree = [0 for _ in range(tree_length + 1)]
    inorder_wright(1)
    print(f"#{test_count}",
          complete_b_tree[1], complete_b_tree[tree_length//2])
