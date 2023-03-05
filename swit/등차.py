등차수열 제일 긴 거 찾기


def solution(arr):
    if len(set(arr)) == 1:
        return len(arr)
    
    else:
        st = 0
        end = 1
        max_len = 1

        diff = arr[1] - arr[0]

        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] == diff:
                end += 1
            else:
                st = i-1
                end = i
                diff = arr[i] - arr[i-1]
            max_len = max(max_len, end-st+1)

        return max_len

    return answer


2이상의 자연수를 두개이상의 자연수의 합으로 나타내는데, 곱이 가장 큰 것
def solution(n):
    arr = [0] * (n+1)
    arr[1] = 1
    
    for i in range(2, n+1):
        for j in range(1, i//2+1):
            arr[i] = max(arr[i], j*(i-j), j*arr[i-j])
            
    return arr[n]

n자리 이진수 중 1을 k개 포함하고 3의 배수인 이진수는 모두 몇개인지 구하라
def create_binary_num(n):
    result = []
    def dfs(idx, binary_num):
        if idx == n:
            result.append(binary_num)
            return

        dfs(idx+1, binary_num + "0")
        dfs(idx + 1, binary_num + "1")

    dfs(0, "")
    
    return result

def solution(N, K):
    answer = 0
    n_binary_num = create_binary_num(N)
    
    for i in n_binary_num:
        if i.count('1') == K:
            if int(f'0b', 2) % 3 == 0:
                answer += 1
        else:
            pass

    return answer