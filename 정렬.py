# 선택 정렬 : 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것
# 삽입 정렬 : 특정한 데이터를 적절한 위치에 삽입
# 실행시간이 더 효율적인 것은 삽입 정렬
# 퀵 정렬 : 가장 많이 쓰는 정렬 방법

# 선택 정렬 소스코드
array = [17, 15, 19, 10, 13, 11, 16, 12, 14, 18]


for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)

# 삽입 정렬 소스코드
array = [17, 15, 19, 10, 13, 11, 16, 12, 14, 18]
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)

# 퀵정렬
array = [15, 17, 19, 10, 13, 11, 16, 12, 14, 18]

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side  = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))