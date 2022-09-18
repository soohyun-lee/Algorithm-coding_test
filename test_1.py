# 단어 정렬

def solution(n):
    word_list = []
    for i in n:
        word_list.append((len(i), i))

    result = sorted(word_list)

    return result