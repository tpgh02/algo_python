import sys
from math import sqrt
input = sys.stdin.readline

def la(n):

    if int(sqrt(n)) == sqrt(n) :
        print(1)
        return
    for i in range(1, int(sqrt(n)) + 1) :
        if int(sqrt(n-i**2)) == sqrt(n-i**2) :
            print(2)
            return
    for i in range(1, int(sqrt(n)) + 1) :
        for j in range(1, int(sqrt(n-i**2)) + 1) :
            if int(sqrt(n-i**2-j**2)) == sqrt(n-i**2-j**2):
                print(3)
                return
    print(4)
    return

n = int(input())

la(n)