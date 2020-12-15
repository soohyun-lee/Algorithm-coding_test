# def solution(n):
#     res = int(n[0])
#     for i in range(len(1,n)):
#         num = int(n[i])
#         if num <= 1 or result <= 1:
#             result += num
#         else:
#             result += num

# print(solution(234234))
 
# # 만들 수 없는 금액 중 최소 금액 찾기
# def solution(n, nums):
#     min_num = min(nums)
#     nums.sort()
#     count = 1
#     for i in nums:
#         if count < i:
#             break
#         count += i
#     return count

# print(solution(5, [1,2,4,5,6]))

# 볼링공 고르기
# 내 풀이

# from itertools import combinations

# def solution(n, m):
#     cnt = 0
#     for i in combinations(m, 2):
#         if i[0] != i[1]:
#             cnt +=1
#         else:
#             continue
#     return cnt

# print(solution(8, [1,5,4,3,2,4,5,2]))

# 답
# def solution(n, m):

array = [0] * 11
print(array)

