import sys
import heapq
input = sys.stdin.readline

hq = []
N = int(input())

for _ in range(N):
    n = int(input())
    
    if n == 0 :
        if len(hq) == 0 :
            print(0)
        else :
            print(heapq.heappop(hq)[1])
    else :
        heapq.heappush(hq, (-n, n))