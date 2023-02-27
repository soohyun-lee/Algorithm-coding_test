n = input()
num = list(map(int, input().split()))

def sum_total(x):
    sum_num=0
    while x > 0:
        sum_num += x%10
        x=x//10

    return x

max_num = -2147000000
for i in num:
    tot = sum_total(i)
    if tot > max_num:
        max_num=tot
        res=i
    
print(res)