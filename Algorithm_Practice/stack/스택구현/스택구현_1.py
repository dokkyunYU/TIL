class Stack:
    def __init__(self, first_data):
        self.stack_data = [first_data]

    def pull(self):
        if self.stack_data == []:
            return None
        return self.stack_data.pop()

    def push(self, any_data):
        self.stack_data.append(any_data)


i = [1, 2, 3, 4, 5]

the_stack = Stack(i[0])  # 1

the_stack.push(i[1])  # 2

print(the_stack.pull())  # 2

the_stack.push(i[2])  # 3

print(the_stack.pull(), the_stack.pull(), the_stack.pull())  # 3 1 None
