# https://www.acmicpc.net/problem/3673
# 부분집합 - 부분집합 = 부분집합
import sys

readline = sys.stdin.readline

for test_cnt in range(int(readline())):
    dividenum, numlen = map(int, readline().split())
    numlist = list(map(lambda x: int(x) % dividenum, readline().split()))

    mod_list = [0 for _ in range(dividenum)]

    sumnow = 0
    for idx in range(numlen):
        sumnow += numlist[idx]
        if sumnow >= dividenum:
            sumnow -= dividenum
        mod_list[sumnow] += 1

    print(sum(map(lambda x: (x * (x - 1)) // 2, mod_list)) + mod_list[0])
