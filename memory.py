# 체스판에서 수평으로 두칸 이동하고 수직으로 한칸 이동하기 / 수직으로 두칸 이동하고 수평으로 한칸 이동하기 
# 이 두가지만 가능하다.

#  8 x 8 좌표에서 현재 나이트가 위치한 곳의 좌표를 준다. 첫째 줄에서 나이트가 이동할 수 있는 경우의 수를 구하라

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

#나이트가 이동할 수 있는 방향
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0 
for step in steps:
    next_row = row + step[0]
    next_column =  column + step[1]
    if next_row >= 1 and next_row <=8 and next_column >=1 and next_column <= 8:
        result += 1

print(result)