import sys
from collections import Counter
input = sys.stdin.readline
n, m, b = map(int, input().split())
tmp_b = b

land = []
for i in range(n):
    land += list(map(int, input().split()))
layer = 0
max_cnt = 6.4 * 10**7

cnt_land = list(dict(Counter(land)).items())

max_key = max(land)
min_key = min(land)

for v in range(min_key, max_key+1):
    cnt = 0
    b = tmp_b
    for i in range(len(cnt_land)):
        num = abs(v - cnt_land[i][0])
        if num == 0 : continue
        if cnt_land[i][0] < v :
            cnt += (num * cnt_land[i][1])
            b -= (num * cnt_land[i][1])
        elif cnt_land[i][0] > v :
            cnt += (2 * num * cnt_land[i][1])
            b += (num * cnt_land[i][1])
    if b<0 :
        continue
    else :
        if cnt < max_cnt :
            max_cnt = cnt
            layer = v
        if cnt == max_cnt :
            if layer < v :
                layer = v

print(max_cnt, layer)