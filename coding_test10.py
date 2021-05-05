m = input()
count = 0
for i in range(len(m)-1):
    if m[i] != m[i+1]:
        count += 1
    
print( (count+1) // 2 )
