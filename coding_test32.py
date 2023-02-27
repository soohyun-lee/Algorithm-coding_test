nums 안에서 두 개의 숫자를 더해서 target이 되는 숫자들이 있다면 해당 숫자들의 인덱스를 반환하는 함수를 작성해주세요. 
Input: nums = [2,7,11,15], target = 9 Output: result = [0, 1]


nums = list(map(int, input().split()))
target = input()

for x in nums:
    