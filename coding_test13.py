import sys
from collections import deque

M, N = list(map(int, input().split()))
print(M)
print(N)
board = [list(map(int, input().split())) for _ in range(M)]

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]


def bfs(x, y, visit):
    q = deque()
    q.append([x, y])

    visit[x][y] = 1
    
    q = 1,0 //
    while q:
        x, y = q.popleft()
        for dir in range(8):
            nx, ny = x + dx[dir], y + dy[dir]

            if 0 <= nx < M and 0 <= ny < N:
                if board[nx][ny] and not visit[nx][ny]:
                    visit[nx][ny] = 1
                    q.append([nx, ny])


def solution():
    answer = 0
    visit = [[0] * N for _ in range(M)]

    for x in range(M):
        for y in range(N):
            if not visit[x][y] and board[x][y]:
                bfs(x, y, visit)
                answer += 1

    return answer


print(solution())