n = int(input())
score = list(map(int, input().split()))

avg = round(sum(score) / n)

minimum = 2147000000

for idx, x in enumerate(score):
    tmp=abs(x-avg)
    if tmp < minimum:
        minimum=tmp
        score=x
        res=idx+1

    elif tmp == minimum:
        if x > score:
            score=x
            res=idx+1