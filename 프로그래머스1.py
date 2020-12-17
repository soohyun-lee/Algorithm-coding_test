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

def solution(arr):
    r = 0
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if arr[y][x]:
                are = min([arr[y-1][x-1], arr[y-1][x],arr[y][x-1]])
                if are and x and y:
                    arr[y][x] == are + 1
                if arr[y][x] > r:
                    r = arr[y][x]
    return r*r


def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = 1 + min(board[i-1], board[i][j-1], board[i-1][j-1])
    m = 0
    for i in board:
        m = max(max(i), m)
    return m ** 2