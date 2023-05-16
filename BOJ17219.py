import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dict = {}

for _ in range(N) :
    site, pw = input().split()
    dict[site] = pw

for _ in range(M) :
    site = input().rstrip()
    print(dict[site])