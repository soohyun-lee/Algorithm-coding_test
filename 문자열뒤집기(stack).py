def reverse_string_with_stack(str1):
    s = []
    revstr = ''

    for i in str1:
        s.append(i)

    while not s.IsEmpty():
        revstr += s.pop()
    
    return revstr

print(reverse_string_with_stack('테스트입니다'))