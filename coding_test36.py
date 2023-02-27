# k번째 수

n, s, e, k = map(int, input().split())

a = list(map(int, input().split()))
a = a[s-1:e]
a.sort()

#평균 구하고 평균이랑 제일 가까운 학생 구하기
n = int(input())
student = list(map(int, input().split()))
avg = sum(student) // n

minimum = 2174000000
for i in range(len(student)):
    if abs(student[i] - avg) < minimum:
        minimum = abs(student[i] - avg)
        res = student[i]

print(i)


# 주어진 자연수 중에서 각 자릿수의 합이 최대인 자연수
n = int(input())
num = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10

    return sum

max_num = -214700000

for x in num:
    tot = digit_sum(x)
    if tot > max_num:
        max_num = tot
        res = x

print(res)

# # 소수의 개수
n = int(input())
ch = [0] * (n+1)
cnt = 0
for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1

print(cnt)

# 뒤집은 소수
n = int(input())
a = list(map(int, input().split()))

def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10

for x in a:
    tmp = reverse(x)

# 문자에서 숫자만 추출하고 약수 갯수 찾기
a = list(map(str, input().split()))
print(a)
b = []

for i in a:
    print(a)
    if i.isdigit():
        b.append(i)
        print(b)
b = ''.join(map(str, b))

# b = int(b)
cnt = 0


# 두리스트 합치기
n = int(input())
n_list = list(map(int, input().split()))
n2 = int(input())
n2_list = list(map(int, input().split()))
c = n_list + n2_list
c.sort()
print(c)


# # 수의 합
n, m = map(int, input().split())
a = list(map(int, input().split()))

lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1

# # 격자판 최대합
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
largest  = -2147000000
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i]a[j]
        sum2 += a[j][i]
    
    if sum1 > largest:
        largest = sum1
    
    if sum2 > largest:
        largest = sum2

sum1 = sum2 = 0

for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]

if sum1 > largest:
    largest = sum1

if sum2 > largest:
    largest = sum2

# # 봉우리
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0] * n)
a.append([0]*n)

for x in a:
    x.insert(0, 0)
    x.append(0)

cnt = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1

print(cnt)


# 정렬하고 타깃 숫자가 인덱스 몇번째인지
n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = n-1
while lt <= rt:
    mid = (lt + rt) // 2
    if a[mid] == m:
        print(mid + 1)
        break
    elif a[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1

# # 그리디 알고리즘 - 회의실 배정 (회의 가장 많이 할 수 있는..)
n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))

meeting.sort(key=lambda x: (x[1], x[0]))
et = 0
cnt = 0

for s, e in meeting:
    if s >= et:
        et = e
        cnt += 1

print(cnt)


# 가장 큰 수 (주어진 갯수 만큼 빼서 큰 수 만들기)
m = map(int, input().split())
num_list = list(map(int, input().split()))

result = []
result.append(num_list[0])
for i in num_list:
    if result[:-1] < i:
        result.pop()
        result.append(i)

# 부분집합 구하기
def DFS(v):
    if v == n+1:
    
    else:
        ch[v] = 1
        DFS(v+1)
        ch[v] = 0
        DFS(v+1)

if __name__ :
    n = int(input())
    ch = [0] * (n+1)
    DFS(1)

n, s, e, k = map(int, input().split())
nums = list(map(int, input().split()))
nums = nums[s-1:e]
nums.sort()
nums[k-1]

# 3장 뽑아서 몇번째로 큰수
nums = list(map(int, input().split()))
res = set()

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            res.add(nums[i] + nums[j] + nums[k])

res = list(res)
res.sort(revers=True)

# 평균에 가장 가까운 학생의 번호
m = int(input())
nums = list(map(int, input().split()))
avg = round(sum(nums) / m)

largest = 2174000000

for idx, x in nums:
    if abs(avg - x) < largest:
        largest = abs(avg - x)
        score = x
        result = idx + 1
    elif abs(avg - x) == largest:
        if x > score:
            score = x
            res = idx + 1

# 정다면체 두개를 합했을 때 경우의 수 가장 많은거
n, m = map(int, input().split())
max = 0
cnt = [0] * (n+m+3)
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1

for i in range(n+m+1):
    if cnt[i] > max:
        max = cnt[i]

for i in range(n+m+1):
    if cnt[i] == max:
        print(i, end= ' ')

# 자릿수의 합
nums = list(map(int, input().split()))
minimum = -2147000000

def getTotal(i):
    while i > 0:
        result += i % 10
        i = i // 10
    return result

for i in range(nums):
    max = getTotal(i)
    if minimum < max:
        minimum == max