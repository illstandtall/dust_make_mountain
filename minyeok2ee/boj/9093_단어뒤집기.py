"""
https://www.acmicpc.net/problem/9093

in
2
I am happy today
We want to win the first prize

out
I ma yppah yadot
eW tnaw ot niw eht tsrif ezirp
"""
import sys

t = int(sys.stdin.readline())

for i in range(t):
    words = list(sys.stdin.readline().split())
    for word in words:
        print(word[::-1], end=" ")
    print()