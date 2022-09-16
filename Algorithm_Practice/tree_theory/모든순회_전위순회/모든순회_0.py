import sys

sys.stdin = open("input.txt")


def preorder_search(node_num):
    if node_num != 0:
        print()
        preorder_search(the_tree[node_num][0])
        preorder_search(the_tree[node_num][1])


def inorder_search(node_num):
    if node_num != 0:
        preorder_search(the_tree[node_num][0])
        print()
        preorder_search(the_tree[node_num][1])


def postorder_search(node_num):
    if node_num != 0:
        preorder_search(the_tree[node_num][0])
        preorder_search(the_tree[node_num][1])
        print()


node_count = int(input())

input_list = list(map(int, input().split()))

the_tree = [[0, 0] for _ in range(node_count + 1)]

answer_list = []

for i in range(len(input_list)):
    if i & 1:
        the_tree[input_list[i - 1]].append(input_list[i])

preorder_search(1)
print(*answer_list)
