import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
mySet = list(range(n+1))

def getParent(list, a):
    if(list[a] == a):
        return a
    list[a] = getParent(list, list[a])
    return list[a]

def unionParent(list, a, b):
    a = getParent(list, a)
    b = getParent(list, b)
    if(a<b): list[b] = a
    else: list[a] = b     
    return list
    
def isSame(list, a, b):
    a = getParent(list, a)
    b = getParent(list, b)
    
    if(a == b): print("YES")
    else : print("NO")

for i in range(m):
    c, a, b = map(int, input().split())
    
    if(c == 0):
        mySet = unionParent(mySet, a, b)
    else :
        isSame(mySet, a, b)