a = [1,2,3,4,5]
b = [1,5,3,2,4,1,2,4,3]

cnt = 0
while True:
    for i in a:
        for y in range(len(b)):
            if i == b[y]:
                cnt += 1
break

print(cnt)
