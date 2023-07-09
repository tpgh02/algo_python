# 접미사

s = input()

strs = []
for i in range(len(s)):
    strs.append(s[i:])

strs.sort()
for ans in strs :
    print(ans)