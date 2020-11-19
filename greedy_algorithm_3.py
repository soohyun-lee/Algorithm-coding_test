# N과 K가 주어질 때, N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구해라
# 1번 : N에서 1을 뺀다.
# 2번 : N을 K로 나눈다.
# 단, 2번의 경우 나누어지는 경우에만 해당

n, k = map(int, input().split())
result  = 0 
while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)