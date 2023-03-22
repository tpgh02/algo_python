import heapq
import sys

input = sys.stdin.readline
n = int(input())

sc = [[]]
q = []

for i in range(n) :
    sc.append(list(map(int, input().split())))
del sc[0]

sc.sort()

heapq.heappush(q, sc[0][1])

for i in range(1, n):
    if sc[i][0] < q[0] :
        heapq.heappush(q, sc[i][1])
    else :
        heapq.heappop(q)
        heapq.heappush(q, sc[i][1])

print(len(q))