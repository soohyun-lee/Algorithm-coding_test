def solution(numbers,target):
    result_list = [0]
    for number in numbers:
        node_list = []
        for tree_number in result_list:
            node_list.append(tree_number + number)
            node_list.append(tree_number - number)
        result_list = node_list
    answer = result_list.count(target)
    return answer

print(solution([1,2,3,6,7], 8))