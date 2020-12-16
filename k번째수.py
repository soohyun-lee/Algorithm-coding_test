# 내 코드
def solution(array, commands):
    answer = []
    for i in commands:
        start = i[0] -1 
        end = i[1]
        mid = i[2] - 1
        sort_array = sorted(array[start:end])
        answer.append(sort_array[mid])

    return answer

# 다른 사람 코드
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))