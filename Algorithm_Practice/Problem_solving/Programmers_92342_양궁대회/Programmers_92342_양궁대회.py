# [Programmers] 92342. 양궁대회
# https://school.programmers.co.kr/learn/courses/30/lessons/92342


def shooting(bullseye, arrows, rivalscore, nowlocation=0, totalsum=0, resultlist=[]):
    global maxsum, maxlist
    if arrows == 0 or nowlocation == 10:
        if (totalsum - rivalscore) > maxsum:
            maxlist = []
            maxsum = totalsum - rivalscore
            maxlist.append(resultlist + [arrows])
        elif (totalsum - rivalscore) == maxsum:
            maxlist.append(resultlist + [arrows])
        return
    if arrows > bullseye[nowlocation]:
        if bullseye[nowlocation]:
            shooting(
                bullseye,
                arrows - bullseye[nowlocation] - 1,
                rivalscore - (10 - nowlocation),
                nowlocation + 1,
                totalsum + 10 - nowlocation,
                resultlist + [bullseye[nowlocation] + 1],
            )
        else:
            shooting(
                bullseye,
                arrows - bullseye[nowlocation] - 1,
                rivalscore,
                nowlocation + 1,
                totalsum + 10 - nowlocation,
                resultlist + [bullseye[nowlocation] + 1],
            )
    shooting(bullseye, arrows, rivalscore, nowlocation + 1, totalsum, resultlist + [0])


def solution(n, info):
    global maxsum, maxlist
    maxsum = 0
    maxlist = []
    infoscore = 0
    for i in range(11):
        if info[i]:
            infoscore += 10 - i
    shooting(info, n, infoscore)
    answer = []
    max_length = 0
    for i in maxlist:
        length = len(i)
        if max_length != max(max_length, length):
            max_length = length
            answer = i
    if len(answer) < 11:
        answer += [0] * (11 - len(answer))
    if maxsum == 0:
        return [-1]
    return answer
