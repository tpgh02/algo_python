# 헌내기는 친구가 필요해
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if(nx<0 or ny<0 or nx>=n or ny>=m or visited[nx][ny] == 1) : continue
        if(collage[nx][ny] == 'X' or collage[nx][ny] == 'I') : continue
        visited[nx][ny] = 1
        if(collage[nx][ny] == 'P') :
            cnt += 1
        dfs(nx, ny)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0

n, m = map(int, input().split())
visited = [[0]*m for _ in range(n)]
collage = []
for _ in range(n):
    collage.append(list(input().rstrip()))
    
for i in range(n):
    for j in range(m):
        if collage[i][j] == 'I' :
            visited[i][j] = 1
            dfs(i, j)
if cnt == 0 :
    print("TT")
else :
    print(cnt)