# 회의 가능한 횟수 계산하기
# 회의의 수와 각 회의의 시작시간, 끝나는 시간이 주어졌을 때, 최대 사용할 수 있는 회의 수 구하기
n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))
meeting.sort(key=lambda x: (x[1], x[0]))
et = 0
count = 0
for s, e  in meeting:
    if s >= et:
        et = e
        count += 1

print(count)