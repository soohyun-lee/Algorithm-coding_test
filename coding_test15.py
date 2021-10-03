# 창영이의 일기장

def solution(words):
    word_list = words.split(" ")
    aeiou = ['a', 'e', 'i', 'o', 'u']
    for k in word_list:
        for i in aeiou:
            if i in k:
                print(k.index(i))
                # print(k[k.index(i) + 1])
                k.replace(k[k.index(i) + 1], '')
                k.replace(k[k.index(i) + 2], '')

            # k.index(i) + 1, k.index(i) + 2
            # print(k.index(i))
            # k.replace(word_list[i.index(k)+1, i.index(k)+2], '')
            
    return k

words_list = 'zepelepenapa papapripikapa'
print(solution(words_list))

# 퇴근하고 풀기 ! 