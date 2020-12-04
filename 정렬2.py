# N명의 학생 정보가 있을 때 성적 낮은 순으로 정렬
# Ex. 
# 2
# 홍길동 95
# 이순신 77 
# 답 : 이순신 홍길동

n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end='')