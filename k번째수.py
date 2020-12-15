# def solution(array, commands):
#     answer = []
#     for i in commands:
#         # for j in i:
#         start = i[0] -1 
#         end = i[1]
#         mid = i[2]
#         array[start:end].sort()
#         answer.append(mid)  
#     return answer

# print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

def solution(array, commands):
    answer = []
    for i in commands:
        start = i[0] -1 
        end = i[1]
        mid = i[2] - 1
        sort_array = sorted(array[start:end])
        answer.append(sort_array[mid])

    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))