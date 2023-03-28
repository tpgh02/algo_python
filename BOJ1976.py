n = int(input())
m = int(input())
node = list(range(n+1))

def getParent(a):
    if node[a] == a :
        return a
    node[a] = getParent(node[a])
    return node[a]

def unionParent(a, b):
    a = getParent(a)
    b = getParent(b)
    if (a<b) : node[b] = a
    else : node[a] = b
    

for i in range(1, n+1):
    edges = list(map(int, input().split()))
    for j in range(len(edges)):
        if edges[j] == 1 :
            unionParent(i, j+1)

canTravel = list(map(int, input().split()))

for i in range(len(canTravel)-1):
    if(getParent(canTravel[i]) != getParent(canTravel[i+1])):
        print("NO")
        break
else:
    print("YES")