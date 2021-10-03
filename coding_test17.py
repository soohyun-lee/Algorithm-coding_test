import sys

A, B = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
answer = 0
result = abs(B - A)

for i in range(N):
    T = abs(B - int(sys.stdin.readline()))

    if T < result:
        answer = 1
        result = T

answer += result

print(answer)