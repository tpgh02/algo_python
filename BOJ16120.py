s = input()
st = []

if s == "P" :
    print("PPAP")
    exit()
for i in range(len(s)):
    st.append(s[i])
    if(st[len(st)-2] == "A"):
        for j in range(4):
            st.pop()
            if (len(st) == 0 and (j != 3)) or s[i] == "A" :
                print("NP")
                exit()
            if j==3 :
                st.append("P")
if(len(st) != 1):
    print("NP")
else :
    print("PPAP")