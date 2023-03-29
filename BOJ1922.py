import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
nodes = []
computers = list(range(n+1))
cost = 0
def getParent(a):
    if computers[a] == a :
        return a
    computers[a] = getParent(computers[a])
    return computers[a]

def unionParent(a, b):
    a = getParent(a)
    b = getParent(b)
    if (a<b) : computers[b] = a
    else : computers[a] = b

for _ in range(m):
    a, b, c = map(int, input().split())
    nodes.append((a, b, c))
    
nodes.sort(key=lambda x:x[2])

for edge in nodes :
    if getParent(edge[0]) == getParent(edge[1]) :
        continue
    cost += edge[2]
    unionParent(edge[0], edge[1])
    
print(cost)