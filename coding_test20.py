# 숫자 추출
import re

string = 'ab1cde4'
numbers = re.sub(r'[^0-9]', '',string)
cnt = 0
for i in range(1, numbers+1):
    if numbers % i == 0:
        cnt += 1
