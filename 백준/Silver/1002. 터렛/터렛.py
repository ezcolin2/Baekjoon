import sys
n=int(input())
for _ in range(n):
    temp=list(map(int, sys.stdin.readline().split()))
    if temp[0]==temp[3] and temp[1]==temp[4] and temp[2]==temp[5]:
        print(-1)
        continue
    distance = (temp[3]-temp[0])**2 + (temp[4]-temp[1])**2
    distance_center =(temp[2]+temp[5])**2
    res = distance-distance_center
    if res>0:
        print(0)
    elif res == 0:
        print(1)
    else:
        res2=distance**0.5+ min(temp[2], temp[5])
        if res2>max(temp[2],temp[5]):
            print(2)
        elif res2==max(temp[2], temp[5]):
            print(1)
        else:
            print(0)