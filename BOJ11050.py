from math import factorial as fact
N, K = map(int, input().split())

print(fact(N) // (fact(K) * fact(N-K)))