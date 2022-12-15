"""
https://www.acmicpc.net/problem/10952

in
1 1
2 3
3 4
9 8
5 2
0 0

out
2
5
7
17
7
"""
import sys

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    print(a+b)