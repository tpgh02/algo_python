n = int(input())

nums = [0, 1, 2]

for i in range(2, n+1):
    nums.append(nums[i-1] + nums[i])

print(nums[n]%10007)