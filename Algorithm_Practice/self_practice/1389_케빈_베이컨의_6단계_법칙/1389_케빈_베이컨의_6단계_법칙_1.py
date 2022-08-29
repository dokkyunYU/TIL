import sys
from collections import deque

sys.stdin = open('input.txt', encoding='utf-8')

people_number, relation_number = [int(k) for k in input().split()]
people_relations_list = [[] for _ in range(people_number + 1)]
for _ in range(relation_number):
    person1, person2 = [int(j) for j in input().split()]
    people_relations_list[person1].append(person2)
    people_relations_list[person2].append(person1)

min_value = 10 ** 6
min_person = 0
for someone in range(1, people_number + 1):
    visited = [0] * (people_number + 1)
    visited_queue = deque()
    visited_queue.append(someone)
    visited[someone] += 1

    while visited_queue:
        person_now = visited_queue.popleft()
        for t in people_relations_list[person_now]:
            if not visited[t]:
                visited[t] = visited[person_now] + 1
                visited_queue.append(t)
    kevin_sum = sum(visited) - people_number
    if min_value > kevin_sum:
        min_value = kevin_sum
        min_person = someone
print(min_person)