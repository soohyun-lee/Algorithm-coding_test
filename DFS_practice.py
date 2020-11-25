# N X M 형태의 직사각형에서 0이 상하좌우로 인접해있으면 하나로 간주, 그래서 총 0이 몇개인지 구하기
# ex. 4 X 5 의 직사각형
# 00110
# 00011
# 11111
# 00000
# >> 0의 갯수는 (상하좌우로 인접해있으면 1개로 취급) : 3개

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x,y):
    if x <= -1 or x >=n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
    
print(result)