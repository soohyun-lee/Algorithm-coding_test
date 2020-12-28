import sys

def solution(prices):
    profit = 0
    min_price = sys.maxsize
    for i in prices:
        min_price = min(min_price, i)
        profit = max(i-min_price, profit)
    return profit

print(solution([1,3,4,6,14,2]))

from collections import deque
def solution(nums):
    new_nums = deque(nums)
    for i in range(len(new_nums)):
        if new_nums.popleft() == new_nums.pop():
            return True
        return False

print(solution([1,2,2,1,5,1,2,2,1]))


# 상하좌우 1로 연결되어 있으면 하나의 땅으로 인식 > 행열에서 땅 몇개 인지 찾기
def islands(n, k):
    
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j <0 or j >= len(grid[0]) or grid[i][j] != 1:
            return
        grid[i][j] = 0

        dfs(i+2, j)
        dfs(i-2, j)
        dfs(i, j-2)
        dfs(i, j+2)
    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs(i, j)
                cnt += 1
    return count

# print(islands([
#     [1,0,1,1,1],
#     [1,1,0,0,0],
#     [0,0,1,1,0]
# ]))
