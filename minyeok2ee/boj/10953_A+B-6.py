"""
https://www.acmicpc.net/problem/10953

in
5
1,1
2,3
3,4
9,8
5,2

out
2
5
7
17
7
"""
import sys

t = int(sys.stdin.readline())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split(","))
    print(a+b)