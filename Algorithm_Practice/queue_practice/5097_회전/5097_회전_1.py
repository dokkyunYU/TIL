import sys

sys.stdin = open("input.txt")

for test_count in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    number_list = input().split()
    print(f"#{test_count}", number_list[m % n])
