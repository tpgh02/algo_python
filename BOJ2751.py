import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []
result = []

for _ in range(N):
    num = int(input())
    heapq.heappush(heap, num)

for i in range(len(heap)):
    result.append(heapq.heappop(heap))
    
for i in result :
    print(i)