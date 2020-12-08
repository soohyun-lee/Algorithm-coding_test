# 프로그래머스 실패율 계산하기

def solution(N, stages):
    result = {}
    stages_len = len(stages)
    for stage in range(1, N+1):
        if stages_len != 0:
            count = stages.count(stage)
            result[stage] = count / stages_len
            stages_len -= count
        else:
            result[stage] = 0   
    return sorted(result, key=lambda x: result[x], reverse=True)

