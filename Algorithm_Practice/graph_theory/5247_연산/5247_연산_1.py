for test_count in range(1, int(input()) + 1):
    start_num, target_num = map(int, input().split())
    calcul_count = 0
    while start_num < target_num:
        start_num *= 2
        calcul_count += 1
