# N : 배열의 크기, M : 숫자가 더해지는 횟수, K : 연속해서 K번을 초과해서 더 할 수 없음

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
    
print(result)