import sys
from math import factorial
from collections import Counter
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    d = {}
    cnt = 1
    for _ in range(n):
        name, kind = input().split()
        d[name] = kind
    kind = Counter(d.values()).values()
    for k in kind :
        cnt *= k+1
    print(cnt-1)