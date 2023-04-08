import sys
input = sys.stdin.readline

n = int(input())
tList = sorted(list(map(int, input().split())))
for i in range(n-1):
    tList[i+1] += tList[i]
print(sum(tList))