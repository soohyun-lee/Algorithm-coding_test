def solution(progresses, speeds):
    answer = []
    while progresses:
        days = 1
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        cnt = 0
        while progresses:
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                cnt += 1
            else:
                break
        if cnt:
            answer.append(cnt)
    return answer