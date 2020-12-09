n = int(input())
people_list = []

for i in range(n):
    h, l = map(int, input().split())
    people_list.append((h, l))
people_list.sort(reverse=True)
max_l = 0
cnt = 0
for x, y in people_list:
    if y > max_l:
        max_l = y
        cnt += 1     
print(cnt)
