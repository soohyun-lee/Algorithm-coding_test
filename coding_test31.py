
m = int(input())
num = list(map(int, input().split()))
stack = []

for x in num:
    # while m == 0:
    if len(a) != 0:
        if a[-1] > x:
            pass
        else:
            del a[-1]
            a.append(x)
            m -= 1


print(a)


for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    
    stack.append(x)

if m != 0:
    stack = stack[:-m]

res = ''.join(map(str, stack))