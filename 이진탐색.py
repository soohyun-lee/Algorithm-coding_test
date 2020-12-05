def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# n개의 원소 갯수와 찾고자 하는 값 입력 받고,
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다')
else:
    print(result + 1)


# 문제
# 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다.
# 두번째 줄에 떡의 개별 높이가 주어진다.
# 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에서 설정할 수 있는 높이의 최대값을 구하라

n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))


start = 0
end = max(array)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid :
            totle += x - mid
    
    if totla < m:
        end = mid - 1

    else:
        result = mid
        start = mid + 1

print(result)