"""
https://www.acmicpc.net/problem/10828

in1
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top

out1
2
2
0
2
1
-1
0
1
-1
0
3

in2
7
pop
top
push 123
top
pop
top
pop

out2
-1
-1
123
123
-1
-1
"""
import sys

n = int(sys.stdin.readline())

stack = []
for i in range(n):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])