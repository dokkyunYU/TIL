# 3
# 234*5/+
# 6528-2/*+
# 325*-42/+2-

import sys

sys.stdin = open('input.txt')

for test_count in range(1, int(input()) + 1):
    calculate_string = input()
    number_stack = []
    for i in calculate_string:
        if i == "+":
            number_stack.append(number_stack.pop() + number_stack.pop())
        # 스택 특성상 먼저 pop된 데이터가 더 뒤의 데이터이므로 -, /은 특별히 처리한다.
        elif i == "-":
            number_stack.append(-number_stack.pop() + number_stack.pop())
        elif i == "*":
            number_stack.append(number_stack.pop() * number_stack.pop())
        # 스택 특성상 먼저 pop된 데이터가 더 뒤의 데이터이므로 -, /은 특별히 처리한다.
        elif i == "/":
            number_stack.append(1 / number_stack.pop() * number_stack.pop())
        else:
            number_stack.append(int(i))
        # print(number_stack)
    # 연산이 올바르게 종료되었다면, 스택 안에는 계산이 완료된 하나의 값만 남아있어야하므로 그냥 출력할 수 있다.
    print(f"# {test_count}", *number_stack)
