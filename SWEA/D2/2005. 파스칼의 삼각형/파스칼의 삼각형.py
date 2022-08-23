def pascal_triangle(number):
    pasacal_list = [[1] for _ in range(11)]
    pasacal_list[2] += [1]
    if number > 2:
        for i in range(3, number + 1):
            for j in range(len(pasacal_list[i - 1]) - 1):
                pasacal_list[i].append(pasacal_list[i - 1][j] + pasacal_list[i - 1][j + 1])
            pasacal_list[i].append(1)
    for k in range(1, number + 1):
        print(*pasacal_list[k])


T = int(input())

for test_count in range(1, T + 1):
    N = int(input())
    print(f"#{test_count}")
    pascal_triangle(N)