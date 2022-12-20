"""
https://www.acmicpc.net/problem/10828

in
15
push 1
push 2
front
back
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
front

out
1
2
2
0
1
2
-1
0
1
-1
0
3
"""
import sys

n = int(sys.stdin.readline())

queue = []
for i in range(n):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == 'push':
        queue.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue = queue[1:]
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif cmd[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])