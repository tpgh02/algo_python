# 프린터큐
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    
    w = deque(map(int, input().split()))
    
    for i in range(n):
        w[i] = [w[i], i]
        
    cnt = 0
    
    while True :
        for i in range(1, len(w)):
            if w[0][0] < w[i][0]:
                w.append(w.popleft())
                break
        else :
            cnt += 1
            if m == w[0][1] :
                print(cnt)
                break
            w.popleft()