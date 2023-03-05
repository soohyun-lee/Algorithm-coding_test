# 전체 은행의 개수 n, 은행 간의 송금 수수료 정보 fees, 돈을 보내려는 은행의 번호 dest가 매개변수로 주어질 때, 돈을 송금하는데 필요한 최소 수수료를 return하는 함수를 작성해줘. fees는 송금 합의가 된 은행간의 수수료 정보를 나타내. fees길이가 3인 배열이며 [a,b,c] 이고, a와 b는 송금 합의가 된 두 은행의 번호이며 c는 두 은행사이의 수수료야. 돈은 항상 1번 은행에서 송금해야해.

# 제일 쉬운 코드로 작성해줘
def solution(n, fees, dest):
    max_num = 2174000000
    arr = [[max_num] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        arr[i][i] = 0

    for a, b, c in fees:
        arr[a][b] = c
        arr[b][a] = c
    
    for i in range(1, n + 1):
        for k in range(1, n + 1):
            for j in range(1, n + 1):
                arr[k][j] = min(arr[k][j], arr[k][i] + arr[i][j])
    
    return arr[1][dest]