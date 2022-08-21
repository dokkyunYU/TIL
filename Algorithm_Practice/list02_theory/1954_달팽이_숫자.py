# 바깥을 둘러싸고 있는 사각형의 크기는 내부 사각형의 크기를 뺀것과 같다
# N**2 - (N-2)**2
# N이 1,2일때는 리스트를 만들고, 그보다 클 경우는 N-2로 다시 스스로를 재귀적으로 호출하여
# 가장 바깥을 둘러싸게 만드는 함수를 제작하면 된다.

from pprint import pprint


def snail_list(given_number):
    if given_number < 1:
        print("1이상의 양수만 입력해주세요.")
        return False
    if given_number == 1:
        return [1]
    if given_number == 2:
        return [[1, 2], [4, 3]]
    if given_number > 2:
        prev_list = snail_list(given_number - 2)
        next_list = [[0] * given_number for _ in range(given_number)]

        # 리스트에 넣을 숫자
        insert_number = 0
        # 첫 행을 채우는 반복문
        for i in range(given_number):
            insert_number += 1
            next_list[0][i] = insert_number
        # 마지막 열을 채우는 반복문
        for j in range(1, given_number):
            insert_number += 1
            next_list[j][given_number - 1] = insert_number
        # 마지막 행을 역순으로 채우는 반복문
        for k in range(1, given_number):
            insert_number += 1
            next_list[given_number - 1][given_number - 1 - k] = insert_number
        # 첫 열을 인덱스 [0][0]을 제외하고 역순으로 채우는 반복문
        for h in range(1, given_number - 1):
            insert_number += 1
            next_list[given_number - 1 - h][0] = insert_number

        # N-2로 호출했던 리스트를 불러와 지금까지 넣었던 숫자중 마지막 숫자를
        # 불러온 리스트의 모든 요소에 더해가며 남아있던 빈 리스트를 채우는 반복문
        for ix in range(1, given_number - 1):
            for iy in range(1, given_number - 1):
                if prev_list == [1]:
                    next_list[ix][iy] = 1 + insert_number
                else:
                    next_list[ix][iy] = prev_list[ix - 1][iy - 1] + insert_number

        return next_list


T = int(input())
for test_count in range(1, T + 1):
    N = int(input())
    print(f"#{test_count}")
    print(i for i in range(10))
    for line_by_line in snail_list(N):
        print(*line_by_line)


#####  Dev.J #####
##### 제출일 : 2019-03-07 02:43 #####
##### 참고용으로 가져온 다른 사람의 코드 #####


res = []
for t in range(int(input())):
    N = int(input())
    arr = [[0 for i in range(N)] for i in range(N)]
    cnt = N
    num, row, col, sw = 0, 0, -1, 1

    while cnt > 0:

        for i in range(cnt):
            num += 1
            col += sw
            arr[row][col] = num

        cnt -= 1

        for i in range(cnt):
            num += 1
            row += sw
            arr[row][col] = num

        sw = -sw
    str_res = ""
    for i in range(N):
        for j in range(N):
            str_res += str(arr[i][j]) + " "
        str_res += "\n" if i < N - 1 else ""
    res.append(str_res)

for i in range(len(res)):
    print("#{}\n{}".format(i + 1, res[i]))
