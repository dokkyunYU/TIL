oper = {'*': lambda x, y: x*y, '+': lambda x, y: x +
        y, '-': lambda x, y: x-y, '/': lambda x, y: x//y}
for t in range(10):
    n = int(input())
    ops = []
    vals = [0]*(n+1)
    for _ in range(n):
        a = input().split()
        a[0] = int(a[0])
        if a[1].isdigit():
            a[1] = int(a[1])
            vals[a[0]] = a[1]
        else:
            a[2] = int(a[2])
            a[3] = int(a[3])
            ops.append(a)
    while ops:
        i, v, a, b = ops.pop()
        vals[i] = oper[v](vals[a], vals[b])
    print(f'#{t+1} {vals[1]}')


# func = lambda x : x + 1
# func(4)
# 5
# 람다함수는 객체이므로 변수를 통해 참조하거나 리스트, 딕셔너리 등의 요소가 될 수 있다
