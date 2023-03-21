n, m = map(int, input().split())

lList = list(map(int, input().split()))
lList.sort()

cnt = 0           
while len(lList) != 0 :
    if ((min(lList))**2 < (max(lList))**2) or min(lList) > 0 :
        if cnt == 0:
            cnt += max(lList)
        else :
            cnt += 2 * max(lList)
        max_index = lList.index(max(lList))
        for i in range(m) :
            if(len(lList) == 0):
                break
            if lList[max_index-i] < 0 :
                break
            del lList[max_index-i]
    else :
        if cnt == 0:
            cnt -= min(lList)
        else :
            cnt -= 2 * min(lList)
        min_index = lList.index(min(lList))
        for i in range(m) :
            if(len(lList) == 0):
                break
            if lList[min_index] > 0 :
                break
            del lList[min_index]

print(cnt)