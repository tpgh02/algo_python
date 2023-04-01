import sys

input = sys.stdin.readline
n, m = map(int, input().split())
tList = list(map(int, input().split()[1:]))
node = list(range(n+1))

for t in tList :
    node[t] = 0

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

cnt=0
parties = []
for i in range(m):
    att = list(map(int, input().split()[1:]))
    for j in range(len(att)-1):
        unionParent(att[j], att[j+1])
    parties.append(att)
    
    
for party in parties:
    know = False
    for i in range(len(party)):
        if getParent(party[i]) == 0 :
            know = True
            break
    if know == False :
        cnt += 1

print(cnt)