import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mList = [0] * n
for i in range(n):
  mList[i] = int(input())

cnt = 0
while m != 0 :
  for i in range(n-1, -1, -1):
    if m >= mList[i] :
        c = m // mList[i]
        m -= mList[i] * c
        n = i+1
        cnt += c
        break
print(cnt)
