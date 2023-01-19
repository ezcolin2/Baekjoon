import sys
n=int(sys.stdin.readline())
nums=list(map(int, sys.stdin.readline().split()))
operators=list(map(int, sys.stdin.readline().split()))
res=[]
maxi=-1e9
mini=1e9
def cal():
    temp=nums[0]
    for i in range(n-1):
        if res[i]==0:
            temp+=nums[i+1]
        if res[i]==1:
            temp-=nums[i+1]
        if res[i]==2:
            temp*=nums[i+1]
        if res[i]==3:
            if temp<0 and nums[i+1]>0:
                temp=-(abs(temp)//nums[i+1])
            else:
                temp//=nums[i+1]
    global maxi
    global mini
    maxi=max(maxi, temp)
    mini=min(mini, temp)

def oper():
    if len(res)==n-1:
        cal()
    for i in range(4):
        if operators[i]>0:
            operators[i]-=1
            res.append(i)
            oper()
            operators[i]+=1
            res.pop()
oper()
print(maxi)
print(mini)