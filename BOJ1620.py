import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dict = {}
for i in range(1, N+1) :
    dict[i] = input().rstrip()

dict2 = {v:k for k, v in dict.items()}

for _ in range(M) :
    try :
        s = input().rstrip()
        s = int(s)
        print(dict[s])
    except :
        print(dict2[s])