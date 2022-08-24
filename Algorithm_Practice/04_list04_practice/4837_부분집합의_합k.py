# 1~12까지 원소를 가지는 집합에서 크기가 N인 부분집합을 추출할때 그 총합이 K인 모든 집합의 수를 찾아라
# 첫줄에 테스트 케이스 수, 둘째줄에 부분집합 크기 N과 부분집합의 합 K가 주어진다


import sys

sys.stdin = open("input.txt")

numbers_list = list(range(1, 13))

T = int(input())

for test_count in range(1, T + 1):
    N, K = map(int, input().split())
    subset_count = 0
    for i in range(1 << 12):
        subset_members = 0
        subset_sum = 0
        for j in range(12):
            # 각 자리수를 검토하며 1일 경우 리스트에서 그 인덱스의 요소를 더해나감
            if i & (1 << j):
                subset_members += 1
                subset_sum += numbers_list[j]
        # 부분집합 크기가 N이고 부분집합 총합이 K라면 subset_count를 1 증가
        if subset_members == N and subset_sum == K:
            subset_count += 1

    print(f"#{test_count} {subset_count}")

# 1.00
