import sys

sys.stdin = open("input.txt")

for test_count in range(1, 11):  # int(input()) + 1):
    string_length = int(input())
    infix_string = input()
    postfix_stack = []
    postfix_string = ""
    for token in infix_string:
        if not postfix_stack or token == "(":
            postfix_stack.append(token)
        elif token in ["*", "/"]:
            if postfix_stack and postfix_stack[-1] in ["*", "/"]:
                postfix_string += postfix_stack.pop()
            postfix_stack.append(token)
        elif token in ["+", "-"]:
            while postfix_stack and postfix_stack[-1] != "(":
                postfix_string += postfix_stack.pop()
            postfix_stack.append(token)
        elif token == ")":
            while postfix_stack and postfix_stack[-1] != "(":
                postfix_string += postfix_stack.pop()
            postfix_stack.pop()
        else:
            postfix_string += token
    while postfix_stack:
        postfix_string += postfix_stack.pop()

    calculate_string = postfix_string
    number_stack = []
    for i in calculate_string:
        if i == "+":
            number_stack.append(number_stack.pop() + number_stack.pop())
        elif i == "-":
            number_stack.append(-number_stack.pop() + number_stack.pop())
        elif i == "*":
            number_stack.append(number_stack.pop() * number_stack.pop())
        elif i == "/":
            number_stack.append(1 / number_stack.pop() * number_stack.pop())
        else:
            number_stack.append(int(i))
    print(f"#{test_count}", *number_stack)