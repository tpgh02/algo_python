import sys
input = sys.stdin.readline

n = int(input())
l = [1, 2, 4]
for i in range(0, 8):
    l.append(l[i] + l[i+1] + l[i+2])
for _ in range(n):
    print(l[int(input())-1])