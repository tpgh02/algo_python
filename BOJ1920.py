import sys
input = sys.stdin.readline

n = int(input())
an = set(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))

for i in num :
    if i in an :
        print(1)
    else :
        print(0)