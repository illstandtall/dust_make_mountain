"""
https://www.acmicpc.net/problem/1406

in1
abcd
3
P x
L
P y

out1
abcdyx

in2
abc
9
L
L
L
L
L
P x
L
B
P y

out2
yxabc

in3
dmih
11
B
B
P x
L
B
B
B
P y
D
D
P z

out3
yxz

"""
import sys

left = list(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline())
right = []
for i in range(m):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'L':
        if len(left) != 0:
            right.append(left.pop())
    elif cmd[0] == 'D':
        if len(right) != 0:
            left.append(right.pop())
    elif cmd[0] == 'B':
        if len(left) != 0:
            left.pop()
    elif cmd[0] == 'P':
        left.append(cmd[1])

res = ''.join(left) + ''.join(right[::-1])
print(res)

## 시간초과 코드
# import sys

# left = sys.stdin.readline().rstrip()
# m = int(sys.stdin.readline())
# right = ""
# for i in range(m):
#     cmd = sys.stdin.readline().split()
#     if cmd[0] == 'L':
#         if len(left) != 0:
#             left, right = left[:-1], left[-1] + right
#     elif cmd[0] == 'D':
#         if len(right) != 0:
#             left, right = left + right[0], right[1:]
#     elif cmd[0] == 'B':
#         left = left[:-1]
#     elif cmd[0] == 'P':
#         left += cmd[1]

# print(left+right)