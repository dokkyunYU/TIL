def is_this_danzo(num: int) -> int:
    str_num = str(num)
    prv_num = 0
    for t in str_num:
        if prv_num > int(t):
            return 0
        prv_num = int(t)
    return 1


for test_count in range(1, int(input()) + 1):
    n = int(input())
    number_list = [int(k) for k in input().split()]
    max_value = -1
    for i in range(n):
        for j in range(i + 1, n):
            mult_num = number_list[i] * number_list[j]
            if is_this_danzo(mult_num) and max_value < mult_num:
                max_value = mult_num
    print(f"#{test_count}", max_value)