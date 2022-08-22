# import sys

# sys.stdin = open("input.txt")

# 간단히 요약해서, 컴퓨터가 연산을 처리해야하는 순서대로 표기하는것이 후위표기법이라고 할 수 있다
# 덧셈 뺄셈은 곱셈과 나눗셈보다 나중에 처리되므로 더 후위에 온다
# 괄호 내부의 식은 더 먼저 처리되어야하므로 더 전위에 온다
# 2+3*4/5 =>> 234*5/+
# (6+5*(2-8)/2) =>> 6528-*2/+
# 3-2*5+4/2-2 =>> 325*-42/+2-
# (3 + 1) / (2 - 4) + 7 * 3 / 2 =>> 31+24-/73*2/+


for test_count in range(1, 11): # int(input()) + 1):
    # string_length = int(input())
    infix_string = input()
    postfix_stack = []
    postfix_string = ""
    for i in infix_string:
        if i == "(":
            postfix_stack.append(i)
        elif i in ["+", "-", "*", "/"]:
            if i in ["*", "/"]:
                if postfix_stack and postfix_stack[-1] in ["*", "/"]:
                    postfix_string += postfix_stack.pop()
                postfix_stack.append(i)
            elif i in ["+", "-"]:
                while postfix_stack and postfix_stack[-1] != "(":
                    postfix_string += postfix_stack.pop()
                postfix_stack.append(i)
        elif i == ")":
            while postfix_stack and postfix_stack[-1] != "(":
                postfix_string += postfix_stack.pop()
            postfix_stack.pop()
        else:
            postfix_string += i
    while postfix_stack:
        postfix_string += postfix_stack.pop()
    print(f"#{test_count}", postfix_string)
