from collections import deque
 
a, b, c = map(int, input().split())
nums = deque([])
ans = a
if b == 1 :
    print(a % c)
    exit()

while True:
    if b == 1 :
        break
    if b % 2 == 0 :
        b = b // 2
        nums.appendleft([2])
    else :
        b = (b-1)//2
        nums.appendleft([2, 1])
for n in nums :
    if len(n) == 1 :
        ans = (ans ** 2) % c
    else :
        ans = ((ans ** 2) * a) % c
print(ans)