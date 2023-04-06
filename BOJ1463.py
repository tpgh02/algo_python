import sys
n = int(sys.stdin.readline())

dp = [1000000, 0, 1, 1]
for i in range(4, n+1):
    div2 = 0 
    div3 = 0
    if i % 2 == 0 :
        div2 = i // 2
    if i % 3 == 0 :
        div3 = i // 3
    dp.append(min(dp[i-1], dp[div2], dp[div3])+1)

print(dp[n])