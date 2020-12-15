def solution(n):
    res = int(n[0])
    for i in range(len(1,n)):
        num = int(n[i])
        if num <= 1 or result <= 1:
            result += num
        else:
            result += num

print(solution(234234))
 
# 만들 수 없는 금액 중 최소 금액 찾기
def solution(n, nums):
    min_num = min(nums)
    nums.sort()
    count = 1
    for i in nums:
        if count < i:
            break
        count += i
    return count

print(solution(5, [1,2,4,5,6]))



