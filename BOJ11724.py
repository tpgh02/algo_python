import sys
from collections import Counter
input = sys.stdin.readline

def getParent(a):
    if g_list[a] == a :
        return a
    g_list[a] = getParent(g_list[a])
    return g_list[a]

def unionParent(a, b):
    a = getParent(a)
    b = getParent(b)
    if (a<b) : g_list[b] = a
    else : g_list[a] = b

N, M = map(int, input().split())

graph = []
g_list = list(range(N+1))

for i in range(M):
    v, e = map(int, input().split())
    graph.append((v, e))
    
graph.sort()
graph.sort(key=lambda x:x[1])

for i in range(M):
    unionParent(graph[i][0], graph[i][1])

print(len(Counter(g_list))-1)