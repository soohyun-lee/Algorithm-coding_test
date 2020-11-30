lists = []
visited = []
def solve(n):
    visited.append(n)
    #print(n, lists[n])
    for i in lists[n]:
        if i not in visited:
            solve(i)

n = int(input())
e = int(input())

for i in range(n+1):
    lists.append([])

for i in range(e):
    a, b = map(int, input().strip().split())
    lists[a].append(b)
    lists[b].append(a)

solve(1)
if 1 in visited:
    visited.remove(1)
print(len(visited))
