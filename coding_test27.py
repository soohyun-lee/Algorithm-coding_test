
T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a=a[s-1:e]
    a.sort()
    print(a[k-1])