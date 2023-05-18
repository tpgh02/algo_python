import sys
input = sys.stdin.readline

n = int(input())

paper = []

white = 0
blue = 0

for _ in range(n):
    paper.append(list(map(int, input().split())))
    
def re(x, y, N):
    global white, blue
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                re(x, y, N//2)
                re(x, y+N//2, N//2)
                re(x+N//2, y, N//2)
                re(x+N//2, y+N//2, N//2)
                return
    if color == 0 :
        white += 1
    else :
        blue += 1
        
re(0, 0, n)
print(white)
print(blue)