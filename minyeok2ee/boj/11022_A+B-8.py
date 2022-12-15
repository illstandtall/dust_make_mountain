"""
https://www.acmicpc.net/problem/11022

in
5
1 1
2 3
3 4
9 8
5 2

out
Case #1: 1 + 1 = 2
Case #2: 2 + 3 = 5
Case #3: 3 + 4 = 7
Case #4: 9 + 8 = 17
Case #5: 5 + 2 = 7
"""
import sys

t = int(sys.stdin.readline())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #"+ str(i+1)+":", a, "+", b, "=", a+b)