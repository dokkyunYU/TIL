# 1315 1324 1337 1439

import sys

sys.stdin = open("input.txt")

T = int(input())

for test_count in range(1, T + 1):
    code_string = [i for i in input() if i in ["(", "{", ")", "}"]]
    is_this_correct = False
    string_stack = ["0", code_string[0]]
    if code_string[0] in [")", "}"]:
        pass
    else:
        for i in range(1, len(code_string)):
            if (code_string[i] == ")" and string_stack[-1] == "(") or (
                code_string[i] == "}" and string_stack[-1] == "{"
            ):  #
                string_stack.pop()
            elif (code_string[i] == ")" and string_stack[-1] == "{") or (
                code_string[i] == "}" and string_stack[-1] == "("
            ):
                break
            else:
                string_stack.append(code_string[i])
        if len(string_stack) == 1:
            is_this_correct = True
    print(f"#{test_count}", int(is_this_correct))
