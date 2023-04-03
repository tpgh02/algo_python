import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    s = list(input())
    s.remove('\n')
    num1 = 0
    num1_index = 0
    num2 = 0
    num2_index = 0
    for i in range(len(s)-1, 0, -1):
        if s[i-1] < s[i] :
            num1 = s[i-1]
            num1_index = i-1
            break
    if num1 == 0 :
        print(''.join(s))
        continue
    for i in range(len(s)-1, 0, -1):
        if num1 < s[i] :
            num2 = s[i]
            num2_index = i
            break
    s[num1_index], s[num2_index] = s[num2_index], s[num1_index]
    s[num1_index+1:] = sorted(s[num1_index+1:])
    print(''.join(s))