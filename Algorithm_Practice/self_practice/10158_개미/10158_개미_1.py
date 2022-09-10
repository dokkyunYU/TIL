# 개미
# https://www.acmicpc.net/problem/10158
# 1858

width, height = map(int, input().split())
p, q = map(int, input().split())
walking_time = int(input())
np = (
    abs(width - p - (walking_time % width))
    if (walking_time // width) & 1
    else p + (walking_time % width)
)
nq = (
    abs(height - q - (walking_time % height))
    if (walking_time // height) & 1
    else p + (walking_time % height)
)
if np > width:
    np = width - (np % width)
if nq > height:
    nq = height - (nq % height)

print(p, q)
