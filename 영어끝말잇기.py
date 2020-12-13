def solution(n, words):
    wrong = 0
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
            wrong = i+1
            break
    if wrong == 0:
        return [0,0]
    if wrong % n == 0:
        return [n, wrong//n]
    else:
        return [wrong%n, (wrong//n)+1]