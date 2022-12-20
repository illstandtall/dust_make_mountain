"""
https://www.acmicpc.net/problem/9012

in1
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(

out1
NO
NO
YES
NO
YES
NO

in2
3
((
))
())(()

out2
NO
NO
NO

"""
import sys

t = int(sys.stdin.readline())

for i in range(t):
    st = []
    string = sys.stdin.readline()
    for s in string:
        if s == '(':
            st.append(1)
        elif s == ')':
            if len(st) == 0:
                print('NO')
                break
            else:
                st.pop()
    else:
        if len(st) == 0:
            print('YES')
        else:
            print('NO')
            