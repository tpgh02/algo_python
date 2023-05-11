import heapq
import sys
input = sys.stdin.readline
n = int(input())

q = []
out = []

for _ in range(n):
    x = int(input())
    
    if x != 0:
        heapq.heappush(q, x)
    else :
        if len(q) != 0 :
            print(heapq.heappop(q))
        else :
            print(0)