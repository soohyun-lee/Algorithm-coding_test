def solution(e, f, c):
    change = e + f
    drink = 0
    while change >= c:
        drink += change // c
        change = change // c + change % c
    return drink

print(solution(12,0,5))