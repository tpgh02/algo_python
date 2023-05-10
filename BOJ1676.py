n = int(input())
if n == 0 :
  n+=1
num = 1
for i in range(1, n+1):
  num *= i
num = ''.join(reversed(list(str(num))))
cnt = 0

for s in num :
  if s == '0':
    cnt += 1
  if s != '0' and cnt != 0 :
    break
print(cnt)