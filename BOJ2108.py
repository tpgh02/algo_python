# 통계학
import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort()
cnts = Counter(nums).most_common()

print(round(sum(nums)/n))
print(nums[n//2])
if n == 1 :
    print(nums[0])
elif cnts[0][1] == cnts[1][1] :
    print(cnts[1][0])
else : 
    print(cnts[0][0])
print(nums[n-1] - nums[0])