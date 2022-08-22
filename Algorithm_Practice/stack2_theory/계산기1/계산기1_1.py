# 3
# 234*5/+
# 6528-2/*+
# 325*-42/+2-

# import sys

# sys.stdin = open('input.txt')

for test_count in range(1, int(input()) + 1):
    calculate_string = input()
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
        # print(number_stack)
    print(f"# {test_count}", *number_stack)
