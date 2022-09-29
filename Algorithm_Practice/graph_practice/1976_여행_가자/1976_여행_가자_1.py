def find_set(node):
    if node != parents_list[node]:
        parents_list[node] = find_set(parents_list[node])
    return parents_list[node]


cities_count = int(input())
travel_count = int(input())
cities_list = [list(map(int, input().split())) for _ in range(cities_count)]
travel_plan = list(map(int, input().split()))
parents_list = list(range(cities_count+1))
for i in range(cities_count):
    for j in range(cities_count):
        if cities_list[i][j] == 1:
            root1, root2 = find_set(i+1), find_set(j+1)
            if root1 > root2:
                parents_list[root1] = root2
            elif root1 < root2:
                parents_list[root2] = root1

prev_city = travel_plan[0]
for i in travel_plan[1:]:
    if parents_list[i] != parents_list[prev_city]:
        print("NO")
        break
    prev_city = i
else:
    print("YES")
