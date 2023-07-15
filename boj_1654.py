# https://www.acmicpc.net/problem/1654

firstnum, lastnum = map(int, input().split())

firstlist = [int(input()) for _ in range(firstnum)]

min = 1
max = max(firstlist)