# # 더해서 target값을 만드는 인덱스 출력
def solution(nums, target):
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

print(solution([1,2,4,3,19,6,7], 11))

def solution(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i
    
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]

print(solution([1,2,4,3,19,6,7], 11))

def solution(nums):
    benefit = 0
    for i in range(len(nums)):
        if nums[i+1] > nums[i]:
            result += prices[i+1] - prices[i]
    return result