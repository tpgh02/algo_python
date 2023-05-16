import sys
input = sys.stdin.readline

n = int(input())
S = set()
for _ in range(n):
    li = input().split()
    cal = li[0]
    if len(li) == 2 :
        num = int(li[1])
    
    if cal == "add" :
        S.add(num)
    elif cal == "remove" :
        S.discard(num)
    elif cal == "check" :
        if num in S :
            print(1)
        else :
            print(0)
    elif cal == "toggle" :
        if num in S :
            S.remove(num)
        else :
            S.add(num)
    elif cal == "all" :
        S.update(range(1, 21))
    else :
        S = set()
        