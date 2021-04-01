n = int(input()) 
costs = [0 for _ in range(n+1)] 

# print('costs : ', costs)

for i in range(1, n+1): 
    costs[i] = list(map(int, input().split())) 
    print('costs : ', costs[i])
    
for i in range(2, n+1): 
    costs[i][0] = costs[i][0] + min(costs[i-1][1], costs[i-1][2]) 
    costs[i][1] = costs[i][1] + min(costs[i-1][0], costs[i-1][2]) 
    costs[i][2] = costs[i][2] + min(costs[i-1][0], costs[i-1][1]) 

print(min(costs[n][0], costs[n][1], costs[n][2]))

