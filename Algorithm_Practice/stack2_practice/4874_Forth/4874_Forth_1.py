# 1340 1414

import sys

sys.stdin = open('input.txt')

for test_count in range(1, int(input()) + 1):
    # 10 이상의 수도 처리하기 위해 리스트 사용
    calculate_string: list = input().split()
    number_stack = []
    result = ""
    for i in calculate_string:
        if i in "+-*/":
            # 연산자가 나왔는데 number_stack에 숫자가 그보다 더 적은 경우 error
            if len(number_stack) < 2:
                result = "error"
                break
            elif i == "+":
                number_stack.append(number_stack.pop() + number_stack.pop())
            elif i == "-":
                number_stack.append(-number_stack.pop() + number_stack.pop())
            elif i == "*":
                number_stack.append(number_stack.pop() * number_stack.pop())
            # 나누어 떨어짐을 표현하기 위해 int 변환
            elif i == "/":
                number_stack.append(int(1 / number_stack.pop() * number_stack.pop()))
        # .이 나와서 결과값을 내야하는데 number_stack에 숫자가 2개 이상일 경우 error
        elif i == ".":
            if len(number_stack) != 1:
                result = "error"
                break
            else:
                result = str(number_stack[0])
                break
        # 위 문자들을 제외한 모든 숫자들은 number_stack에 push
        else:
            number_stack.append(int(i))

    print(f"#{test_count}", result)
