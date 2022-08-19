# 04_거리두기 확인하기
# https://school.programmers.co.kr/learn/courses/30/lessons/81302
# 1445
import sys

sys.stdin = open("input.txt")


def solution(places):
    answer = []
    all_is_well = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    nx = 0
    ny = 0
    nx2 = 0
    ny2 = 0
    for waiting_place in places:
        all_is_well = True
        for x in range(5):
            for y in range(5):
                if waiting_place[x][y] == "P":
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < 5 and 0 <= ny < 5:
                            if waiting_place[nx][ny] == "P":
                                all_is_well = False
                                break
                            elif waiting_place[nx][ny] != "X":
                                for t in range(4):
                                    nx2 = nx + dx[t]
                                    ny2 = ny + dy[t]
                                    if (
                                        0 <= nx2 < 5
                                        and 0 <= ny2 < 5
                                        and (nx2 != x or ny2 != y)
                                    ):
                                        if waiting_place[nx2][ny2] == "P":
                                            all_is_well = False
                                            break
                        if all_is_well == False:
                            break
                if all_is_well == False:
                    break
            if all_is_well == False:
                break
        answer.append(int(all_is_well))
    return answer


rere = []
for _ in range(5):
    rere.append(input().split())
print(solution(rere))
