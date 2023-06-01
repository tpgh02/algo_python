n = int(input())

for _ in range(n):
    lis = list(input())
    st = []
    
    for i in range(len(lis)):
        if lis[i] == '(' :
            st.append('(')
        else :
            if len(st) == 0 :
                print('NO')
                break
            st.pop()
    else :
        if len(st) == 0 :
            print("YES")
        else :
            print("NO")
    