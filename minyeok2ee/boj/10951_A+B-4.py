"""
https://www.acmicpc.net/problem/10951

in
1 1
2 3
3 4
9 8
5 2

out
2
5
7
17
7
"""
import sys

lines = sys.stdin.readlines()

for line in lines:
    a, b = map(int, line.split())
    print(a+b)