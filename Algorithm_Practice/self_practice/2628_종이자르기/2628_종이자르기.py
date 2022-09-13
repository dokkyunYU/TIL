# BoJ - 종이자르기
import sys

sys.stdin = open("input.txt")

square_width, square_height = map(int, input().split())

width_slice = [0]
height_slice = [0]

for _ in range(int(input())):
    slicing_where, slicing_numbers = map(int, input().split())
    if slicing_where == 0:
        height_slice.append(slicing_numbers)
    else:
        width_slice.append(slicing_numbers)

width_slice.append(square_width)
height_slice.append(square_height)

width_slice.sort()
height_slice.sort()

width_piece = []
height_piece = []

n = len(width_slice)
m = len(height_slice)

for i in range(n - 1):
    width_piece.append(width_slice[i + 1] - width_slice[i])
for j in range(m - 1):
    height_piece.append(height_slice[j + 1] - height_slice[j])

max_value = max(width_piece) * max(height_piece)
print(max_value)
