def solution(array):
    count = 0
    for i in array:
        count += 1
        if count == 10:
            break

print(solution('addddewdfwfwqefwfewf'))


import collections

def solution(sentence):
    sentence = sentence.replace(',','').split()
    answer = []
    for i in sentence:
        answer.append(i)
    counts = collections.Counter(answer)
    return counts.most_common(1)[0][0]

def solution(word):
    word = word.sort()