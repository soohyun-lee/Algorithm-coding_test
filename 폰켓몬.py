# 내 풀이
def solution(nums):
    length = len(nums) // 2
    nums = set(nums)
    if len(nums) <= length:
        return len(nums)
    return length
    
# 다른 사람 풀이
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
