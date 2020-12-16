def solution(array, m, k):
    array = sorted(array, reverse=True)
    result = 0
    while True:
        for i in range(k):
            if m == 0:
                break
            result += int(array[0])
            m -= 1
        if m == 0:
            break
        result += int(array[1])
        m -= 1
    return result 

print(solution([2,4,5,4,6], 8, 3))

def solution(array):
    result = []
    for i in array:
        result.append.(min(i))
    return max(result)

