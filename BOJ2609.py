a, b = map(int, input().split())

ac = a
bc = b
cd = 1
i = 2
if a == b :
    print(a)
    print(b)
    exit()
while i < max(a, b) :
    if bc//i == bc/i and ac//i == ac/i :
        bc = bc//i
        ac = ac//i
        cd *= i
    else :
        i += 1
lcm = cd * ac * bc
print(cd)
print(lcm)