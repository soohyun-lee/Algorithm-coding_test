# 내 코드
def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        return 1
    return 0


# 효율성이 높게 나온 다른 사랆 코드
def solution(s):
    result = []
    for i in s:
        if not result:
            result.append(i)

        elif result[-1] == i:
            result.pop()

        else:
            result.append(i)

    return 0 if result else 1