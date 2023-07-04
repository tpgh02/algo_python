import sys

input = sys.stdin.readline

N = int(input())
cost = []
preColor = -1
fCost = 0

for _ in range(N):
    r, g, b = map(int, input().split())
    
    cost.append([r, g, b])

for i in range(1, N):
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0]
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + cost[i][1]
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + cost[i][2]

print(min(cost[N-1]))