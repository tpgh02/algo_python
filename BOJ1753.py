import sys
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
graph = []
visited = [False] * (v+1)
cost = [3000000] * (v+1)


for _ in range(e):
    u, ve, w = map(int, input().split())
    graph.append((u,ve,w))
    if u == k :
        if cost[ve] > w :
            cost[ve] = w
cost[0] = 3000001
cost[k] = 3000001

graph.sort(key=lambda x:x[2])

for i in range(e):
    min = 3000000
    for j in range(v+1):
        if cost[j] < min and visited[j] == False :
            min = cost[j]
            min_index = j # min_index = 2
    visited[min_index] = True
    for j in range(e):
        if graph[j][0] == min_index :
            if visited[graph[j][1]] == False and cost[min_index] + graph[j][2] < cost[graph[j][1]] :
                cost[graph[j][1]] = cost[min_index] + graph[j][2]

for i in range(1, v+1) :
    if cost[i] == 3000001 :
        cost[i] = 0
    if cost[i] == 3000000 :
        cost[i] = "INF"
    print(cost[i])