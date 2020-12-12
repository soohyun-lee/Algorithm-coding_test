# 주어진 두개 단어가 애너그램인지 확인하기

a = input()
b = input()

str1 = dict()
str2 = dict()

for x in a:
    str1[x] = str1.get(x, 0) + 1
for x in b:
    str2[x] = str2.get(x, 0) + 1

for y in str1.keys():
    if y in str2.keys():
        if str1[y] != str2[y]:
            print('no')
            break
    else:
        print('no')
        break
else:
    print('yes')