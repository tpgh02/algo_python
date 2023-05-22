import sys
input = sys.stdin.readline

n = int(input())

l = list(map(int, input().split()))
s = sorted(list(set(l))) # [-10, -9, 2, 4]
d = {} # {-10:0, -9:1, 2:2, 4:3}
for i in range(len(s)):
    d[s[i]] = i
    
for i in range(n):
    l[i] = d.get(l[i])

print(*l)