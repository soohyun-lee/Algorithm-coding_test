from collections import deque

n, k = map(int, input().split())
queue = [(pos, val) for pos,val in enumerate(list(map(int, input().split())))]
queue = deque(queue)
cnt = 0
while True:
    cur = queue.popleft()
    if any(cur[1] < x[1] for x in queue):
        queue.append(cur)
    else:
        cnt += 1
        if cur[0] == k:
            break
print(cnt)
