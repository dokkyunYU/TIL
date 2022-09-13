# 중위순회
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV140YnqAIECFAYD
# 2340 2410


import sys


def inorder_search(node_num):
    global result_string
    # 왼쪽 탐색 시도
    try:
        inorder_search(int(the_tree[node_num][2]))
    except IndexError:
        # 없을 경우 그냥 현재 값 입력 후 종료
        result_string += the_tree[node_num][1]
        return
    # 위에서 입력 및 종료가 일어나지 않은 경우, 즉 왼쪽 자식 노드를 탐색하고 돌아온 경우
    result_string += the_tree[node_num][1]
    # 오른쪽 탐색 시도
    try:
        inorder_search(int(the_tree[node_num][3]))
    except IndexError:
        # 없다면 그냥 종료
        return


sys.stdin = open("input.txt", encoding="utf-8")

for test_count in range(1, 11):
    node_count = int(input())
    the_tree = [0]
    result_string = ""
    for _ in range(node_count):
        the_tree.append(input().split())
    inorder_search(1)
    print(f"#{test_count}", result_string)
