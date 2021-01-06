from collections import deque

def solution(n,m,k,x):
    graph = [[] for _ in range(n+1)]
    for _ in range(n):
        a, b = map(int, input().split())
        graph[a].append(b)
    distance = [-1] * (n+1)
    distance[x] = 0
    q = deque([x])
    while q:
        now = q.popleft()
        for next_node in graph[now]:
            if distance[next_node] == -1:
                distance[next_node] = distance[now] + 1
                q.append(next_node)
    for i in range(1, n+1):
        if distance[i] == k:
            return i
        
print(solution(4,4,2,1))