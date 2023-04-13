import sys
input = sys.stdin.readline

n = int(input())
village = [[] * i for i in range(n)]

for i in range(n) :
    village[i] = list((input()).rstrip())

dx = [0, 1, 0, -1, 0]
dy = [1, 0, -1, 0, 0]
global cnt
cnt = 0
numHouse = []

def dfs(x, y):
    global cnt
    for i in range(5):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if ny<0 or nx<0 or nx>= n or ny>=n : continue
        if village[nx][ny] == '0' : continue
        
        village[nx][ny] = '0'
        dfs(nx, ny)
        cnt += 1

for i in range(n):
    for j in range(n):
        if village[i][j] != '0' :
            dfs(i, j)
            numHouse.append(cnt)
            cnt = 0

numHouse.sort()

print(len(numHouse))
for i in numHouse :
    print(i)
