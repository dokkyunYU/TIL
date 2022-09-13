def in_order(value):
    if value <= n:
        in_order(value * 2)
        print(data[value], end="")
        in_order(value * 2 + 1)


for tc in range(1, 11):
    n = int(input())
    data = [0] * (n + 1)
    for i in range(n):
        temp = list(input().split())
        data[i + 1] = temp[1]

    print("#%d" % tc, end=" ")
    in_order(1)
    print()
