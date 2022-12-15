"""
https://www.acmicpc.net/problem/11021

in
5
1 1
2 3
3 4
9 8
5 2

out
Case #1: 2
Case #2: 5
Case #3: 7
Case #4: 17
Case #5: 7
"""
import sys

t = int(sys.stdin.readline())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #"+ str(i+1)+":", a+b)