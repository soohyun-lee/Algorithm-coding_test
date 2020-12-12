# 첫째줄에 자연수가 주어진다.
# 두번째 줄에 노트에 미리 적은 N개의 숫자가 주어지고,
# 그 다음 줄 부터, 시에 쓰인 n-1개의 단어가 주어진다.
# 시에 쓰이지 않은 1개의 단어를 찾아라

# 내 풀이
n = int(input())
word_list = []
use_word = []
for _ in range(n):
    word_list.append(input())
for _ in range(n-1):
    use_word.append(input())

for i in word_list:
    if i not in use_word:
        print(i)

# 강의 풀이
n = int(input())
p = dict()
for i in range(n):
    word = input()
    p[word] = 1
for i in range(n-1):
    word = input()
    p[word] = 0
for key, val in p.items():
    if val == 1:
        print(key)