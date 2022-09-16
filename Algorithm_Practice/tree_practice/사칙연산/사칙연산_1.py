# 사칙연산
# 1457 1558

import sys
sys.stdin = open("input.txt")


# 후위표기식을 사용하여 스택으로 계산한다
def postorder(node_num):
    # 만약 해당 노드에 있는 리스트의 길이가 1보다 크다면
    if len(calculate_tree[node_num]) > 1:
        # 왼쪽과 오른쪽 자식 노드로 차례로 방문한다
        postorder(int(calculate_tree[node_num][1]))
        postorder(int(calculate_tree[node_num][2]))
        # 이후 이 리스트 제일 앞에 있는 연산자에 대응되는 딕셔너리의 람다함수를 불러와서
        # stack에서 pop한 두개의 값들을 계산하여 다시 스택에 넣는다
        calculate_stack.append(
            operator_dict[calculate_tree[node_num][0]](
                calculate_stack.pop(), calculate_stack.pop())
        )
    # 만약 방문한 노드의 리스트가 1보다 크지 않다면, 즉 그냥 숫자 1개의 리스트라면
    else:
        # 계산을 위해 스택에 정수화 해서 집어넣는다
        calculate_stack.append(int(calculate_tree[node_num][0]))


# 람다함수를 value로 가지는 딕셔너리를 정의한다
operator_dict = {"+": lambda x, y: y + x,
                 "-": lambda x, y: y - x,
                 "*": lambda x, y: y * x,
                 "/": lambda x, y: y / x}
for test_count in range(1, 11):
    node_count = int(input())
    calculate_tree = [[] for _ in range(node_count + 1)]
    for _ in range(node_count):
        idx = input().split()
        # 맨 앞의 수를 인덱스로 사용하고, 남은 리스트를 슬라이싱하여 해당 위치에 넣는다
        calculate_tree[int(idx[0])] += idx[1:]
    # 계산을 위한 스택을 선언한다
    calculate_stack = []
    postorder(1)
    # 마지막까지 스택에 남아있는 값이 계산 결과이므로 이를 표시한다
    print(f"#{test_count}", int(calculate_stack[0]))
