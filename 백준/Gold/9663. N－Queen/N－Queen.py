import sys
sys.setrecursionlimit(10000)
n=int(sys.stdin.readline())
row=[]
cnt=0
def can_append(k):
    for i in range(len(row)):
        if abs(len(row)-i)==abs(k-row[i]) or row[i]==k:
            return False
    return True
def dfs():
    global cnt 
    if len(row)==n:
        cnt+=1
    else:
        for i in range(n):
            if can_append(i):
                row.append(i)
                dfs()
                row.pop()
dfs()
print(cnt)
        