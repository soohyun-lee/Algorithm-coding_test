def solution(answers):
    answer = []
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    
    score = [0,0,0]
    result = []
    
    for number in range(len(answers)):
        if answers[number] == first[number%len(first)]:
            score[0] += 1
        if answers[number] == second[number%len(second)]:
            score[1] += 1
        if answers[number] == third[number%len(third)]:
            score[2] += 1    

    for idx, score in enumerate(score):
        if score == max(score):
            result.append(idx+1)
    return result


    # return [k for k,v in all_result.items() if max(all_result.values()) == v] 

