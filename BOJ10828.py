import sys
input =sys.stdin.readline
n = int(input())

st = []

for _ in range(n):
    s = input().split()
    if s[0] == 'push':
        st.append(s[1])
    elif s[0] == 'pop':
        if len(st) == 0 :
            print(-1)
        else :
            print(st[len(st)-1])
            st.pop()
    elif s[0] == 'size':
        print(len(st))
    elif s[0] == 'empty':
        if len(st) == 0 :
            print(1)
        else :
            print(0)
    elif s[0] == 'top':
        if len(st) == 0 :
            print(-1)
        else :
            print(st[len(st)-1])