from collections import deque

need = input()
n = int(input())

for i in range(n):
    plan=input()
    dq=deque(need)

    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("no")
                break
        
    else:
        if len(dq) == 0:
            print("YES")
        
        else:
            print("no")
