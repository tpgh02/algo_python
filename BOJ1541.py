string = input()

num = ''
numlist = []
for i in range(len(string)):
  if string[i] != '-':
    num += string[i]
  else :
    numlist.append(num)
    num = ''
  if i == len(string)-1:
    numlist.append(num)

for j in range(len(numlist)):
  tmp = numlist[j].split('+')
  for i in range(len(tmp)) :
    tmp[i] = tmp[i].lstrip('0')
  numlist[j] = '+'.join(tmp)

for i in range(len(numlist)):
  numlist[i] = str(eval(numlist[i]))
print(eval('-'.join(numlist)))