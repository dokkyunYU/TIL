# 전위순회
# 2420 2443
import sys

sys.stdin = open("input.txt")


def preorder_search(node_num):
    answer_list.append(node_num)
    if the_tree[node_num]:
        preorder_search(the_tree[node_num][0])
        try:
            preorder_search(the_tree[node_num][1])
        except IndexError:
            return


node_count = int(input())

input_list = list(map(int, input().split()))

the_tree = [[] for _ in range(node_count + 1)]

answer_list = []

for i in range(len(input_list)):
    if i & 1:
        the_tree[input_list[i - 1]].append(input_list[i])

preorder_search(1)
print(*answer_list)
