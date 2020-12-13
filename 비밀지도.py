# 나의 풀이
def solution(d, budget):
    cnt = 0
    num = 0
    if sum(d) > budget:
        d = sorted(d)
        for i in d:
            num += i
            cnt += 1
            if num > int(budget):
                cnt -= 1
                break
        return cnt
    else:
        return len(d)

# 다른 사람의 풀이
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)