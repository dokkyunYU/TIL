# [Programmers] 92342. 양궁대회
# https://school.programmers.co.kr/learn/courses/30/lessons/92342

def shooting(bullseye, arrows, nowlocation=0, totalsum=0, resultlist=[]):
    global maxsum, maxlist
    if arrows == 0 or nowlocation == 10:
        if totalsum > maxsum:
            maxsum = totalsum
            maxlist = resultlist
        return
    if arrows > bullseye[nowlocation]:
        shooting(bullseye, arrows - bullseye[nowlocation] - 1, nowlocation + 1, totalsum + 10 - nowlocation, resultlist + [bullseye[nowlocation] + 1])
    shooting(bullseye, arrows, nowlocation + 1, totalsum, resultlist + [0])


def solution(n, info):
    global maxsum, maxlist
    maxsum = 0
    infoscore = 0
    for i in range(11):
        if info[i]:
            infoscore += 10 - i
    shooting(info, n)
    print(maxsum, maxlist)
    answer = []
    return answer