import sys

input = sys.stdin.readline
n = int(input())

cList = []

for _ in range(n):
    s, t = map(int, input().split())
    cList.append((s, t))

cList.sort(key=lambda x: x[0])
cList.sort(key=lambda x: x[1])
cnt = 1
end = cList[0][1]
for i in range(1, n):
    if cList[i][0] >= end :
        cnt += 1
        end = cList[i][1]
        
print(cnt)