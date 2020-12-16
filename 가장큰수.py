def solution(numbers):
    number = "".join(map(str, numbers))
    print(number)
    b = sorted(number, reverse=True)
    print(b)
    result = "".join(map(str, b))
    return result

print(solution([3, 30, 34, 5, 9]))

numbers = [1,33,54,9,3]
number = list(map(str, numbers))
print('number:', number)

print('이건 뭘까:', number.sort(key=lambda x: x*3, reverse=True))
print(str(int(''.join(number))))


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))