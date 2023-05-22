import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))

for i in range(1, n):
    l[i] += l[i-1]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    if a == 0 :
        print(l[b])
    else :
        print(l[b] - l[a-1])