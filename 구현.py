#구현 1
def solution(n, plans):
    x, y = 1, 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    plan = ['L', 'R', 'U', 'D']

    for i in plans:
        for j in range(len(plan)):
            if i == plan[j]:
                nx = x + dx[j]
                ny = y + dy[j]
        if  nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x, y = nx, ny
    return (nx, ny)
    
print(solution(11, ['R', 'R', 'R', 'U', 'D', 'D']))

#구현 2
def solution(n):
    dic = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
    plans = [(1,2), (-1,2), (1,-2), (-1,-2), (2,1), (-2,1), (2,-1), (-2,-1)]
    cnt = 0
    x = int(dic[n[0]])
    y = int(n[1])
    for i in plans:
        row = x + i[1]
        col = y + i[0]
        if row >= 1 and row <= 8 and col >= 1 and col <= 8:
            cnt += 1
    return cnt

print(solution('c2'))
