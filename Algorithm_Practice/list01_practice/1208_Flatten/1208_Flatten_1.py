# Flatten
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh

import sys

sys.stdin = open("input.txt")

T = 10

for i in range(1, T + 1):
    dump_numbers = int(input())
    box_heights = list(map(int, input().split()))

    for j in range(dump_numbers + 1):
        max_box_idx = 0
        min_box_idx = 0
        max_box_height = box_heights[0]
        min_box_height = box_heights[0]

        for k in range(len(box_heights)):
            # 최대값보다 크면 최대값 갱신하고 인덱스 저장
            if box_heights[k] > max_box_height:
                max_box_height = box_heights[k]
                max_box_idx = k
            # 최소값보다 작으면 최소값 갱신하고 인덱스 저장
            if box_heights[k] < min_box_height:
                min_box_height = box_heights[k]
                min_box_idx = k
        # 이미 평탄화 되었을 경우 빠져나감
        if max_box_height - min_box_height <= 1:
            break
        # 그렇지 않을 경우 평탄화하고, dump횟수가 다 되더라도 같은 높이의 박스가 여러개 존재할 경우를 대비하여 한번 더 최대값 최소값 계산
        elif j < dump_numbers:
            box_heights[max_box_idx] -= 1
            box_heights[min_box_idx] += 1
        else:
            break

    print("#{} {}".format(i, max_box_height - min_box_height))
