# 숫자의 표현


def expressions(num):
    answer = 0
    for i in range(1, num+1):
        sum_val = 0
        for j in range(i, num+1):
            sum_val += j
            if sum_val == num:
                answer += 1
                break
            elif sum_val > num:
                break

    return answer