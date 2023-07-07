# 사용할 좌표 리스트
# 빈 리스트들을 요소로 가지는 이중 리스트를 구현
coordinate_list = [[[] for _ in range(31)] for _ in range(31)]

# [0][0]을 원점으로 좌표는 각 15씩 더하면 됨
T = int(input())
for test_case in range(1, T + 1):
    supply1_location = []
    supply2_location = []
    min_distance = 10**6
    house_amount = int(input())
    # 집을 구분하기 위해 집 번호를 매겨서 리스트 마지막에 추가
    house_location_and_distance = [list(map(int, input().split())) + [t] for t in range(house_amount)]
    # 리스트에 맞는 좌표로 변환 -> 좌표 (-15,-15)를 리스트의 [0][0]으로 설정
    for k in range(house_amount):
        # x좌표에 15를 더함
        house_location_and_distance[k][0] += 15
        # y좌표에 15를 더함
        house_location_and_distance[k][1] += 15
    # 좌표 리스트에 변환된 좌표의 위치로 집 번호를 int로 대입
    for kk in house_location_and_distance:
        coordinate_list[kk[0]][kk[1]] = kk[3]

    for i in range(31):
        for j in range(31):
            # 좌표 리스트 전체를 순회하며, 그 안에 든 것이 정수가 아니라 list타입일때(즉 집이 아니고)
            # 그 좌표와 각 집과의 거리를 구하여 그 거리가 집과 충전소 사이의 거리와 작거나 같은지 확인후
            # 조건 만족하면 집의 번호를 해당 좌표의 빈 리스트에 추가
            for house in house_location_and_distance:
                if (
                        type(coordinate_list[i][j]) == list
                        and 0 < abs(house[0] - i) + abs(house[1] - j) <= house[2]
                ):
                    coordinate_list[i][j].append(house[3])
            # 집번호가 다 추가되었을때 모든 집번호가 있는 좌표가 있다면 그 좌표들로 리스트 생성
            if (
                    type(coordinate_list[i][j]) == list
                    and len(coordinate_list[i][j]) == house_amount
            ):
                supply1_location.append((i, j))
            # 집번호가 다 추가 되었을때 아무 집번호든지 있는 좌표가 있다면 모두 포함해 리스트 생성
            if (
                    type(coordinate_list[i][j]) == list
                and coordinate_list[i][j]
            ):
                # 해당 좌표값과, 그 좌표에 저장된 집번호 리스트로 튜플을 만들어 리스트 저장
                supply2_location.append((i, j, coordinate_list[i][j]))

    # 만약 모든 곳에 연결되는 충전소를 놓을 수 있다면
    if supply1_location:
        # 모든 집에서부터 이 충전소와의 거리를 구하여 최소값 갱신
        for supply in supply1_location:
            local_distance_sum = 0
            for house2 in house_location_and_distance:
                local_distance_sum += abs(supply[0] - house2[0]) + abs(supply[1] - house2[1])
            if local_distance_sum < min_distance:
                min_distance = local_distance_sum
    # 1개로 불가능하다면
    else:
        # 각 집과 연결되는 모든 좌표들의 리스트를 조합으로 검토
        for t1 in range(len(supply2_location)):
            for t2 in range(t1 + 1, len(supply2_location)):
                local_distance_sum2 = 0
                # 모든 집을 연결할 충전소 2개의 좌표가 있다면
                if len(set(supply2_location[t1][2] + supply2_location[t2][2])) == house_amount:
                    # 각 집에서부터 충전소1과 충전소2의 거리를 각각 구하여 더 작은 쪽을 부분합에 더해나감
                    for house3 in house_location_and_distance:
                        distance1 = abs(supply2_location[t1][0] - house3[0]) + abs(supply2_location[t1][1] - house3[1])
                        distance2 = abs(supply2_location[t2][0] - house3[0]) + abs(supply2_location[t2][1] - house3[1])
                        local_distance_sum2 += distance1 if distance1 < distance2 else distance2
                        # 더하던 중 이미 이전 최소값을 초과했다면 진행중이던 과정을 무시하고 반복문 종료
                        if local_distance_sum2 > min_distance:
                            break
                    # 반복문 종료후 이전 최소값과 비교하여 더 작은 쪽으로 최소값 갱신
                    if local_distance_sum2 < min_distance:
                        min_distance = local_distance_sum2

    # 최소값이 변화 없이 그대로인 경우 -1을 출력하고, 아닌 경우 그 최소값을 출력
    print("#{} {}".format(test_case, min_distance if min_distance != 10**6 else -1))

    # 사용한 좌표 리스트를 다시 최초 상태로 초기화
    for ii in range(31):
        for jj in range(31):
            coordinate_list[ii][jj] = []