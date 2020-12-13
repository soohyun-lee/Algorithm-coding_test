#가로가 x, 세로가 y 인 직사각형을 대각선 방향으로 잘랐을 때, 선이 지나지 않은 멀쩡한 사각형(1cm X 1cm) 의 갯수 구하기

from math import gcd
def solution(w,h):
    return (w * h) - (w + h - gcd(w,h))
