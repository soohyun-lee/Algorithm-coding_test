def solution(nums):
    length = len(str(nums))
    first = 0
    end = 0
    for i in range(length//2):
        first += int(nums[i])
    for y in range(length//2, length):
        end += int(nums[y])
    if first == end:
        return 'LUCKY'
    return 'READY'

print(solution('123303'))

def solution(n):
    num = 0
    new = []
    sort_list = sorted(n)
    for i in sort_list:
        if i.isalpha():
            new.append(i)
        else:
            num += int(i)
    new.append(str(num))
    return ''.join(new)

print(solution('K1KA5CB7'))