cooking_time = int(input()) 

a=b=c=d=n=0

a = cooking_time // 300 
n = cooking_time % 300 

b = n  // 60 
n = n % 60 

c = n // 10 
n = n % 10 

if (n != 0):
    print(-1) 
print(a,b,c)

