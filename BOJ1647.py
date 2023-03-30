import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nodes = []
village = list(range(n+1))

def getParent(a):
    if village[a] == a :
        return a
    village[a] = getParent(village[a])
    return village[a]

def unionParent(a, b):
    if(a<b) : village[b] = a
    else : village[a] = b

for _ in range(m):
    a, b, c = map(int, input().split())
    nodes.append((a, b, c))

nodes.sort(key=lambda x:x[2])

cnt = 0
end = 0
for node in nodes :
    # if len(set(village)) == 3 : --> 이부분을 빼니 시간초과가 나지 않는다. 시간복잡도가 그렇게 큰가??
    #     break
    aParent = getParent(node[0])
    bParent = getParent(node[1])
    if aParent != bParent :
        unionParent(aParent, bParent)
        cnt += node[2]
        end = node[2]

print(cnt - end)