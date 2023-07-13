# https://www.acmicpc.net/problem/1436

startnum = 666

cnt = 1
target = int(input())
while cnt < target:
    startnum += 1
    if "666" in str(startnum):
        cnt += 1

print(startnum)
