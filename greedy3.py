# 창고의 길이 L
# L 개의 자연수 : a
# 높이 조정 횟수 : m
# m 회의 높이 조정을 마친 후 가장 높은 곳과 낮은 곳의 차이 구하기
L = int(input())
a = list(map(int, input().split()))
m = int(input())

a.sort()
for _ in range(m):
    a[0] += 1
    a[L-1] -+ 1
    a.sort()

print(a[L-1] - a[0])


# 데크 사용
# N 명의 승객과 N 명의 승객의 각 몸무게가 주어진다.
# 보트 한개에 탈 수 있는 총 무게도 M 으로 주어진다.
# N 명의 승객의 몸무게는 M 을 넘지 않으며 몸무게는 50 이상, 150 이하 이다.
# N 명의 승객이 탈출하기 위한 최소 갯수의 구명보트 구하기
from collections import deque

n, m = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
p = deque(p)
cnt = 0

while p:
    if len(p) == 1:
        cnt += 1
        break

    if p[0] + p[-1] > m:
        p.pop()
        cnt +=1
    else:
        p.popleft()
        p.pop()
        cnt += 1

print(cnt)
