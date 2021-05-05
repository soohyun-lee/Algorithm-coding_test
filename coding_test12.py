# 내 풀이

num_list = list(map(str, input().split()))


def results(number_list):
    number_list.sort()
    for i in range(len(num_list)-1):
        if num_list[i] in num_list[i+1]:
            return False
    return True


print(results(num_list))


# 다른 사람 풀이
num_list = list(map(str, input().split()))

def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    print(phoneBook)
    for i in phoneBook:
        print(type(i))
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print(p1, p2)
        if p2.startswith(p1):
            return False
    return True


print(solution(num_list))

