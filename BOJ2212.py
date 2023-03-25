n = int(input())
k = int(input())
if(k>=n):
    print(0)
    exit()
sensor = list(map(int, input().split()))
sensor.sort()

diff = [sensor[i+1] - sensor[i]for i in range(n-1)]

diff.sort(reverse=True)

for _ in range(k-1):
    del diff[0]

print(sum(diff))