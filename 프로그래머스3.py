def solution(answers):
    new = []
    cnta = 0
    cntb = 0
    cntc = 0
    a = [1, 2, 3, 4, 5] * 9999
    b = [2, 1, 2, 3, 2, 4, 2, 5] * 9999
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 9999
    for i in range(len(answers)):
        if answers[i] == a[i]:
            cnta += 1
    new.append(cnta)
    print(new)
    for i in range(len(answers)):
        if answers[i] == b[i]:
            cntb +=1
    new.append(cntb)
    print(new)
    for i in range(len(answers)):
        if answers[i] == c[i]:
            cntc +=1
    new.append(cntc)
    print(new)
    return sorted(new)

print(solution([1,2,3,4,5,4,3,4,3,2]))