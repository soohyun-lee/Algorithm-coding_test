from collections import deque

n, k = map(int, input().split())
queue = list(range(1, n+1))
queue = deque(queue)


while queue:
    for _ in range(k-1):
        n = queue.popleft()
        queue.append(n)
    queue.popleft()
    if len(queue) == 1:
        print(queue[0])
        break
