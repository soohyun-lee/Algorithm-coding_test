# n 개의 행과, M개의 열이 존재하며 행 별로 가장 작은 숫자를 찾고, 그 숫자 중에 제일 큰 숫자 찾기

n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)