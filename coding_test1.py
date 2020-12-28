# 가장 높은 지점까지의 빗물 쌓기

def solutin(height):
    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left], left_max),
                              max(height[right], right_max)
        if left_max <= right_max:
            volume += left_ma - height[left]
            left +=1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume

# 세 개의 숫자를 합해서 0 나오는 숫자 리스트 출력
def threesum(nums):
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                results.append((nums[i], nums[left], nums[right]))

                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -+ 1
                left += 1
                right -= 1  

    return results

print(threesum([-1,0,1,-2,-1,-4]))

# 
import collections

def solution(nums):
    return max(sum(collections(nums, 2)))

# 자신을 제외한 숫자 곱한 배열 출력
def solutiin(nums):
    out = []
    p = 1
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    p = 1
    for i in range(len(nums)-1, 0-1m -1):
        out[i] = out[i] * p
        p = p * nums[i]
    return out
