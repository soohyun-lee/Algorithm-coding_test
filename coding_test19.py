n = int(input())

for i in range(n):
    s=input()
    s=s.upper()
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print('false')
            break
    else:
        print('true')


for i in range(n):
    s=input()
    s=s.upper()
    if s == s[::-1]:
        print('true')
    else:
        print('false')