from collections import deque

n = input()
cnt = int(input())

for i in range(cnt):
    plan = input()
    dq = deque(n)
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print('NO')
                break
    else:
        if len(dq) == 0:
            print('YES')
        else:
            print('NO')

