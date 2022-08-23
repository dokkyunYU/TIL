### 순열 ###

from itertools import permutations

numbers = [1, 2, 3, 4]
length = 3  # 뽑고 싶은 원소의 개수

for line in permutations(numbers, length):
    print(line)


### 조합 ###

from itertools import combinations

numbers = [1, 2, 3, 4]
length = 3  # 뽑고 싶은 원소의 개수

for line in combinations(numbers, length):
    print(line)
