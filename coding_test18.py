# k번째 큰 수 (3개의 숫자를 더해서 k번째 큰 수 찾기)
n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i] + a[j] + a[m])


res = list(res)
res.sort(reverse=True)
print(res[k-1])
