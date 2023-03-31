import sys
input = sys.stdin.readline

def getParent(a):
    if lights[a] != a :
        lights[a] = getParent(lights[a])
    return lights[a]

def unionParent(a, b):
    a = getParent(a)
    b = getParent(b)
    if (a<b) : lights[b] = a
    else : lights[a] = b

while True:
    n, m = map(int,input().split())
    if n == 0 and m == 0 :
        break
    nodes = []
    lights = list(range(n))
    cost = 0
    totalCost = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        totalCost += c
        nodes.append((a, b, c))
        
    nodes.sort(key=lambda x:x[2])

    for edge in nodes :
        if getParent(edge[0]) == getParent(edge[1]) :
            continue
        cost += edge[2]
        unionParent(edge[0], edge[1])

    print(totalCost - cost)