# 주어진 숫자를 최소한의 횟수로 나눠서 1 만들기
# 2,3,5 로 나누며 나누어지지 않을 때는 1 빼기
x = int(input())
d = [0] * 300

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i //2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
print(d[x])


def mergesort(s):