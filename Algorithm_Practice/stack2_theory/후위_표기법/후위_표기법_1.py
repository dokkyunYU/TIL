import sys

sys.stdin = open("input.txt")

# 간단히 요약해서, 컴퓨터가 연산을 처리해야하는 순서대로 표기하는것이 후위표기법이라고 할 수 있다
# 덧셈 뺄셈은 곱셈과 나눗셈보다 나중에 처리되므로 더 후위에 온다
# 괄호 내부의 식은 더 먼저 처리되어야하므로 더 전위에 온다
# 2+3*4/5 =>> 234*5/+
# (6+5*(2-8)/2) =>> 6528-*2/+
# 3-2*5+4/2-2 =>> 325*-42/+2-
# (3 + 1) / (2 - 4) + 7 * 3 / 2 =>> 31+24-/73*2/+


for test_count in range(1, 11):  # int(input()) + 1):
    # string_length = int(input())
    infix_string = input()
    postfix_stack = []
    postfix_string = ""
    for token in infix_string:
        # 스택이 비었거나 혹은 토큰이 여는 괄호라면 그냥 스택에 넣는다.
        if not postfix_stack or token == "(":
            postfix_stack.append(token)
            # 토큰이 * 혹은 / 일때, 스택 내부의 자신보다 우선순위가 높거나 같은 연산자들을 전부 pop하면서 더 낮은 우선순위 중 하나를 만날때까지 나아간다.
        elif token in ["*", "/"]:
            if postfix_stack and postfix_stack[-1] in ["*", "/"]:
                postfix_string += postfix_stack.pop()
            # 이후 현재 토큰은 스택에 넣는다.
            postfix_stack.append(token)
        # 토큰이 + 혹은 - 일때, 스택 내부의 자신보다 우선순위가 높거나 같은 연산자들을 전부 pop하면서 더 낮은 우선순위 중 하나를 만날때까지 나아간다.
        elif token in ["+", "-"]:
            while postfix_stack and postfix_stack[-1] != "(":
                postfix_string += postfix_stack.pop()
            # 이후 현재 토큰은 스택에 넣는다.
            postfix_stack.append(token)
        # 토큰이 닫는 괄호라면, 여는 괄호를 만날때까지 스택 내부의 자신보다 우선순위가 높거나 같은 연산자들을 전부 pop하면서 나아간다.
        elif token == ")":
            while postfix_stack and postfix_stack[-1] != "(":
                postfix_string += postfix_stack.pop()
            # 이후 여는 괄호는 스택 내부에서 제거한다.
            postfix_stack.pop()
        # 위 분류에 포함되지 않는 모든 토큰들은 그대로 결과 string에 추가한다.
        else:
            postfix_string += token
    # 반복문이 종료되면, 남아있는 스택을 모두 pop하며 결과 string에 추가한다.
    while postfix_stack:
        postfix_string += postfix_stack.pop()
    print(f"#{test_count}", postfix_string)
