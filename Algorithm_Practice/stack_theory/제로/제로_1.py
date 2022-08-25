# 제로
# https://www.acmicpc.net/problem/10773


class Stack:
    def __init__(self):
        self.data_list = []

    def push(self, any_data):
        if any_data == 0:
            self.data_list.pop()
        else:
            self.data_list.append(any_data)

    def all_sum(self):
        return sum(self.data_list)


T = int(input())
# the_stack = Stack 같은 형식으로 선언할 경우 클래스의 인스턴스 객체가 아니라 그냥 그 해당 클래스로 접근한다
the_stack = Stack()
for test_count in range(1, T + 1):
    the_stack.push(int(input()))
print(the_stack.all_sum())
