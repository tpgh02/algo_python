import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline

n = int(input())
m = int(input())

computers = [[] * i for i in range(n+1)]
visited = [False] * (n+1)
q = deque()

def bfs():
    q.appendleft(1)
    visited[1] = True
    
    while len(q) != 0 :
        no = q.popleft()
        
        for i in computers[no] :
            if not visited[i] :
                q.appendleft(i)
                visited[i] = True

for _ in range(m):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a)

bfs()
c = Counter(visited)

print(c[True] -1)