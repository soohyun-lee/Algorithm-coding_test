import sys
input = sys.stdin.readline

N = int(input())
tree = list(map(int, input().split()))

tree.sort(reverse=True)
answer = 0
for i,j in enumerate(tree):
    answer = max(answer, i+j+2)

print(answer)

