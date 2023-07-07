from collections import deque

n = int(input())

stack = deque([[n]])

cnt = 0
ans = []

while True :
    element = []
    for i in range(len(stack[0])) :
        element.append(stack[0][i] - 5)
        element.append(stack[0][i] - 3)
    element = sorted(list(set(element)))
    stack.append(deque(element))
    stack.popleft()
    cnt += 1
    exit = False
    
    while True:
        if stack[0][0] < 3 and stack[0][0] != 0:
            stack[0].popleft()
            if len(stack[0]) == 0 :
                print(-1)
                exit = True
                break
        elif stack[0][0] == 0 :
            print(cnt)
            exit = True
            break
        else :
            break
    if exit :
        break
