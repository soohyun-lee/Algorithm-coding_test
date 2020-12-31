import string

def solution(str1):
    dic = {key: 0 for key in string.ascii_lowercase}
    for i in str1:
        dic[i] += 1
    for key, value in dic.items():
        if value > 1:
            str1 = str1.replace(key, "")
    return str1

print(solution('googggle'))