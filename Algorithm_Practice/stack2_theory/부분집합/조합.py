def combinations(arr, depth):
    # 전체 원소의 개수만큼 재귀가 진행됐다면 종료
    if depth == len(numbers):
        # 뽑고 싶은 만큼 뽑았다면 출력
        if len(arr) == length:
            print(arr)
        return

    # 1) 현재 원소를 뽑고 다음 재귀로 진행하는 경우
    combinations(arr + [numbers[depth]], depth + 1)

    # 2) 현재 원소를 뽑지 않고 다음 재귀로 진행하는 경우
    combinations(arr, depth + 1)


numbers = [1, 2, 3, 4]
length = 3  # 뽑고 싶은 원소의 개수

combinations([], 0)


# 위 방법과 다르게 앞서 나온 재귀 순열 코드와 비슷한 방식으로도 구현 가능하다.

# 단 순열과 달리 조합은 순서가 상관 없기 때문에 start 지점을 두어 이전 원소보다 더 오른쪽에 있는 원소들을 뽑아 나간다.


def combinations(arr, start):
    # 뽑고 싶은 만큼 뽑았다면 출력 및 종료
    if len(arr) == length:
        print(arr)
        return

    for i in range(start, len(numbers)):
        # 1) i번째 원소를 뽑는다.
        arr.append(numbers[i])

        # 2) 재귀함수 진행
        combinations(arr, i + 1)

        # 3) 재귀함수 종료 후, 뽑았던 i번째 원소 삭제
        arr.pop()


numbers = [1, 2, 3, 4]
length = 3  # 뽑고 싶은 원소의 개수

combinations([], 0)
