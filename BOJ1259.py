import sys
input = sys.stdin.readline

while True :
    n = str(int(input()))
    if n == '0':
        break
    
    for i in range(len(n)//2):
        if n[i] != n[-i-1] :
            print("no")
            break
    else :
        print("yes")