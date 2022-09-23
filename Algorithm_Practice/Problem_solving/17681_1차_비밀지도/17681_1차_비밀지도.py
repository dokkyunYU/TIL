# [Programmers] 17681. [1차] 비밀지도


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        maze_string = ""
        for j in range(n - 1, -1, -1):
            maze_string += "#" if arr1[i] & 1 << j or arr2[i] & 1 << j else " "
        answer.append(maze_string)
    return answer
