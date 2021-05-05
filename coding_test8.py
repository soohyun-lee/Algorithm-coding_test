import sys
input = sys.stdin.readline

n, k = map(int, input().split())
kids = list(map(int, input().split()))

result = []
for i in range(1, n):
    result.append((kids[i] - kids[i-1]))

result.sort(revers=True)
print(sum(result[k-1:]))
