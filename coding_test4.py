def letter(digit):
    def dfs(index, path):
        if len(path) == len(digit):
            result.append(path)
            return
        
        for i in range(index, len(digit)):
            for j in dic[digit[i]]:
                dfs()

    if not digit:
        return []
    
    dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
    result = []
    dfs(0, "")

    return result

from itertools import combinations
def solution(n, k):
    return list(combinations(n, k))

def solution(nums, target):
    result = []
    def dfs(csum. index, path):
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return
        for i in range(index, len(nums)):
            dfs(scum )

def solution(nums):
    result = []
    def dfs(index, path):
        result.append(path)
        print(result)
        for i in range(index, len(nums)):
            dfs(i+1, path + [nums[i]])
    dfs(0, [])
    return result

print(solution([1,2]))
def solution(box, capacity):
    result = []
    total_value = 0
    for i in box:
        result.append((i[0] / i[1], i[0], i[1]))
        result.sort(reverse=True)
        print('result :', result)
    for i in result:
        while total_value < capacity:
            total_value += i[2]s
            capacity -= i[2]
    return total_value

print(solution([(4,12),(2,1),(10,4),(1,1),(2,2)],15))
