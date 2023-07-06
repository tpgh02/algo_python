k, n = map(int, input().split())

lan = []

for _ in range(k):
    lan.append(int(input()))

cnt = 0
result = 0
low = 1
high = max(lan)

while(low <= high) :
    line = (low + high) // 2
    for i in range(k):
        cnt += lan[i] // line
    if cnt >= n :
        result = max(result, line)
        low = line + 1
    else :
        high = line - 1
    cnt = 0
print(result)