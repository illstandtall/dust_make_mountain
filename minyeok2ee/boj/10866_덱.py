"""
https://www.acmicpc.net/problem/10866

in1
15
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front

out1
2
1
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
22
front
back
pop_front
pop_back
push_front 1
front
pop_back
push_back 2
back
pop_front
push_front 10
push_front 333
front
back
pop_back
pop_back
push_back 20
push_back 1234
front
back
pop_back
pop_back

out2
-1
-1
-1
-1
1
1
2
2
333
10
10
333
20
1234
1234
20
"""
import sys

n = int(sys.stdin.readline())

deq = []
for i in range(n):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == 'push_front':
        deq = [cmd[1]] + deq
    elif cmd[0] == 'push_back':
        deq = deq + [cmd[1]]
    elif cmd[0] == 'pop_front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
            deq = deq[1:]
    elif cmd[0] == 'pop_back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
            deq.pop()
    elif cmd[0] == 'size':
        print(len(deq))
    elif cmd[0] == 'empty':
        if(len(deq)) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if(len(deq)) == 0:
            print(-1)
        else:
            print(deq[0])
    elif cmd[0] == 'back':
        if(len(deq)) == 0:
            print(-1)
        else:
            print(deq[-1])