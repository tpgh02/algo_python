import sys
input = sys.stdin.readline

n = int(input())
weight = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
box = sorted(list(map(int, input().split())), reverse=True)
cnt = 0
if box[0] > weight[0]:
    print(-1)
else:
    while len(box) > 0:
        cnt += 1
        for i in range(len(weight)) :
            for j in range(len(box)):
                if weight[i] >= box[j] :
                    box.remove(box[j])
                    break
    print(cnt)