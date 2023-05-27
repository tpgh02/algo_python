import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
num = list(range(max(nums)+1))
cnt = 0

for i in range(2, len(num)):
    if num[i] == 0 :
        continue
    
    for j in range(2 * i, len(num), i):
        num[j] = 0
        
num = num[2:]

for i in nums :
    if i in num :
        cnt+=1

print(cnt)