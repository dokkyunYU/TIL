print(*[i.count("@") for i in input().split("(")])


string_count = 0
for j in input():
    if j == "0":
        print(string_count, end=" ")
        string_count = 0
    elif j == "@":
        string_count += 1
print(string_count)

# 0.05
