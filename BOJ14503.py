import sys
input = sys.stdin.readline
global x, y, d, cnt, isFin
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
    
def rotate():
    global d, x, y
    d -= 1
    if d < 0 :
        d = 3
    if d > 3 :
        d = 0

n, m = map(int, input().split())
y, x, d = map(int, input().split())
room = []
isFin = False
for i in range(n) :
    room.append(list(map(int, input().split())))

cnt = 0
while True:
    if room[y][x] == 0:
        room[y][x] = 2
        cnt += 1
    if room[y-1][x] != 0 and room[y+1][x] != 0 and room[y][x-1] != 0 and room[y][x+1] != 0 :
        x = x - dx[d]
        y = y - dy[d]
        if room[y][x] == 1 :
            break
        else :
            continue
    while True :
        rotate()
        if room[y+dy[d]][x+dx[d]] == 0:
            break
    x = x + dx[d]
    y = y + dy[d]
    
print(cnt)