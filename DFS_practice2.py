# n x m 크기의 직사각형 형태의 미로에 갇혀 있고, 한번에 한칸씩만 이동가능하다
# 0이 있는 칸은 가면 안되며 1이 있는 칸으로만 갈 수 있다.
# ex. 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상,하,좌,우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or ny <0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0,0)) 