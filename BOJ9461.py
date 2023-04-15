import sys
input = sys.stdin.readline

T = int(input())



for _ in range(T):
    dp = [1, 1, 1, 2, 2]
    n = int(input())
    
    for i in range(5, n) :
        dp.append(dp[i-5] + dp[i-1])
    print(dp[n-1])