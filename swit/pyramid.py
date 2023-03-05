# 피라미드의 꼭대기 층인 0행부터 마지막 행까지 순서대로 각 행을 구성하는 블록들 중 하나에 대한 정보를 나타내는 2차원 배열 blocks 가 매개변수로 주어집니다. 피라미드를 완성시킨 후, 꼭대기 층 왼쪽부터 제일 아래층 오른쪽까지 순서대로 모두 합친 새로운 배열을 return 하는 함수를 작성해주세요. blocks의 i번째 원소는 피라미드 i행을 구성하는 블록 하나에 대한 정보입니다. blocks 의 원소는 [a,b]형식입니다. a는 왼쪽에서 몇번째 블록인지를 나타내며 i행의 경우 0이상 i 이하의 정수입니다.

def solution(blocks):
    height = len(blocks) - 1
    pyramid = [[0] * (i + 1) for i in range(height + 1)]
    pyramid[0][0] = blocks[0][1]
    
    for i in range(1, height + 1):
        for j in range(i + 1):
            if j == 0:
                pyramid[i][j] = pyramid[i - 1][j] + blocks[i * (i + 1) // 2][1]
            
            elif j == i:
                pyramid[i][j] = pyramid[i - 1][j - 1] + blocks[i * (i + 1) // 2 + j][1]
            
            else:
                pyramid[i][j] = max(pyramid[i - 1][j - 1], pyramid[i - 1][j]) + blocks[i * (i + 1) // 2 + j][1]
    
    result = []
    for i in range(height + 1):
        for j in range(i + 1):
            result.append(pyramid[i][j])
    
    return result