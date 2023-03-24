s = list(input())
s.sort()
stup = sorted(list(set(s)))
isOdd = False
pelin = ""
if len(s) == 1 :
    print(s[0])
    exit()
if len(s) % 2 == 0 :
    for ch in stup :
        if s.count(ch) % 2 != 0 :
            print("I'm Sorry Hansoo")
            exit()
        else :
            for i in range(s.count(ch)//2):
                pelin += ch
    pelin += pelin[::-1]
    print(pelin)
else :
    oddCh = ""
    for ch in stup :
        if s.count(ch) % 2 == 1 and isOdd :
            print("I'm Sorry Hansoo")
            exit()
        elif s.count(ch) % 2 == 1 :
            isOdd = True        
            oddCh += ch
        for i in range(s.count(ch)//2):
            pelin += ch
    pelin += oddCh
    pelin += pelin[len(pelin)-2::-1]
    print(pelin)