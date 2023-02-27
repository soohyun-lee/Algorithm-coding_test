n = int(input())
p=dict()

for i in range(n):
    word=input()
    p[word] = 1

for i in range(n-1):
    word=input()
    p[word] = 0


for k, v in p.items():
    if v != 0:
        print(k)