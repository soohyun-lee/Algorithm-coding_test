# 전화번호부
def solution(phone_book):
    phone_book.sort()
    for a in range(len(phone_book)-1):
        if phone_book[a] in phone_book[a+1]:
            return False
    return True
red = 10
print(int(red**(1/2))+1)


def solution(brown, red):
    nm = brown + red
    for n in range(1, nm+1):
        if nm%n != 0:
            continue
        m = nm//n
        if (n-2)*(m-2) == red:
            return sorted([n, m], reverse = True)