import sys
input=sys.stdin.readline
n=int(input())
arr=[tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x : (-x[0], -x[1]))
days=[0]*(10001)
for p, d in arr:
    for i in range(d, 0,  -1):
        if days[i]==0:
            days[i]=p
            break
print(sum(days))