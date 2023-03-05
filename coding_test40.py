a = input()
b = input()
a = a.upper()
b = b.upper()

a_dict = {}
b_dict = {}

for i in a:
    if i not in a_dict.keys():
        a_dict[i] = 1
    else:
        a_dict[i] += 1

for i in b:
    if i not in b_dict.keys():
        b_dict[i] = 1
    else:
        b_dict[i] += 1

if a_dict == b_dict:
    print("TRUE")
else:
    print("FALSE")