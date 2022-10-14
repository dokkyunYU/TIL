# 러시아 국기 같은 깃발
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQl9TIK8qoDFAXj

for test_count in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    yy = [input() for _ in range(n)]
    min_color = float("inf")
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                coloring = n*m
                for t in yy[:i+1]:
                    coloring -= t.count("W")
                for t in yy[i+1:j+1]:
                    coloring -= t.count("B")
                for t in yy[j+1:]:
                    coloring -= t.count("R")
                if coloring < min_color:
                    min_color = coloring
    print(f"#{test_count}", min_color)