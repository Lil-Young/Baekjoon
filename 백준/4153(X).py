import sys
input = sys.stdin.readline
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0: break
    elif a**2 + b**2 == c**2: print("right")
    else: print("wrong")
    
# https://www.acmicpc.net/problem/4153